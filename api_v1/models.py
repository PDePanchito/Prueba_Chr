from django.db import models

class Network(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class Company(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Station(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    address = models.CharField(max_length=255)

