from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from .models import Network, Company, Station


def apiGet(request):
    api_url = 'https://api.citybik.es/v2/networks/bikerio'

    response = requests.get(api_url)

    api_data = response.json()

    context = {'api_data': api_data}

    return render(request, 'api.html', context)

# Function that saves data to postgresql database
def storeData(request):
    # Replace with your API endpoint URL
    api_url = 'https://api.citybik.es/v2/networks/bikerio'

    response = requests.get(api_url)

    if response.status_code == 200:

        api_data = json.loads(response.content.decode('utf-8'))

        network_data = api_data.get("network")

        network, created = Network.objects.get_or_create(
            name=network_data.get("name"),
            city=network_data.get("location").get("city"),
            country=network_data.get("location").get("country")
        )

        # If a new network was created, store Company and Station information
        if created:
            # Store Company information
            company_data = network_data.get("company")
            for company_name in company_data:
                Company.objects.create(network=network, name=company_name)

            # Store Station information
            station_data = network_data.get("stations")
            station_entries = []
            for station in station_data:
                station_entry = Station(
                    network=network,
                    name=station.get("name"),
                    empty_slots=station.get("empty_slots"),
                    free_bikes=station.get("free_bikes"),
                    address=station.get("extra").get("address")
                )
                station_entries.append(station_entry)

            Station.objects.bulk_create(station_entries)

        return JsonResponse({"status": "success"})

    else:
        return JsonResponse({"status": "failure"})


# Get the information from the database
def databaseGet(request):

    network = Network.objects.first()  

    stations = Station.objects.filter(network=network)

    companies = Company.objects.filter(network=network)

    context = {'network': network,
               'stations': stations, 
               'companies': companies
               }
    
    return render(request, 'bootstrapview.html', context)
