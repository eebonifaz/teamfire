from django.shortcuts import render
from django.http import JsonResponse
import requests
import csv
import json
# Create your views here.


def fire(request):

    server_request = requests.get(
        "https://firms.modaps.eosdis.nasa.gov/active_fire/c6/text/MODIS_C6_South_America_24h.csv")
    response = server_request.content.decode("UTF8")
    result = []
    skip = True
    for row in csv.reader(response.splitlines(), delimiter=','):
        if skip:
            skip = False
            continue
        result.append([row[0], row[1], int(row[8]) / 100])
    return JsonResponse(result, safe=False)
