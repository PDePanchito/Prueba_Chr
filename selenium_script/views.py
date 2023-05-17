from django.shortcuts import render
import json
from .models import Datos

def view_data(request):
    with open('data.json') as json_file:
        data = json.load(json_file)
    return render(request, 'data.html', {'data': data})

def view_table(request):
    data = Datos.objects.all()
    return render(request, 'databootstrap.html', {'data': data})
