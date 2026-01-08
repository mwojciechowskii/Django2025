from django.shortcuts import render, redirect
from .utils import requestJSON
from typing import Optional

DEFAULT_CITY = "Poznan"

def weatherView(request, inputCity: Optional[str] = None):
    """
    uzylem redirect zeby url funkcjonowal jako /weather/<miasto>, 
    inaczej przy wpisywanym inpucie otrzymywalem weather/?City=<miasto>
    """
    
    cityFromPage = request.GET.get("City") 
    if cityFromPage:
        return redirect("weather:cityWeather", inputCity=cityFromPage.strip())

    requestedCity = (inputCity or DEFAULT_CITY).strip()
    context = {}
    url = f'https://wttr.in/{requestedCity}?format=j2'
    try: 
        response = requestJSON(url)
    except Exception as err:
        return render(request, 'weather/index.html', {"error": err, "City": [inputCity, "wrong"]})

    city = response['nearest_area'][0]
    currentWeather = response['current_condition'][0]
    context = {
            'City': city['areaName'][0]['value'],
            'Country': city['country'][0]['value'],
            'Temperature': currentWeather['temp_C'],
            'Pressure': currentWeather['pressure'],
            'localObsDateTime': currentWeather['localObsDateTime'],
            'WeatherDesc': currentWeather['weatherDesc'][0]['value'],
        }

    return render(request, 'weather/index.html', context)
