# Lic. García Héctor
#! python3
# weather.py - Pronóstico meteorológico utilizando API de WeatherApi 

import requests,os,sys,json

if(len(sys.argv)>1):
    city = sys.argv[1]
    APIkey = 'b1aec6b11ab6476faf9221759241002'
    #url = f'http://api.weatherapi.com/v1/current.json?key={APIkey}&q={city}$days=7'
    #url=f'http://api.weatherapi.com/v1/forecast.json?key={APIkey}&q=07112&days=2'
    url = f'http://api.weatherapi.com/v1/forecast.json?key={APIkey}&q={city}&days=7&lang=es'
    res = requests.get(url)
    res.raise_for_status()
    info = res.json()
    predictions = info['forecast']['forecastday']
    for day in predictions:
        date = day['date']
        max_temp_c = day['day']['maxtemp_c']
        min_temp_c = day['day']['mintemp_c']
        condition = day['day']['condition']['text']
        print(f"Fecha: {date}, Máxima: 🌡 {max_temp_c}°C, Mínima: {min_temp_c}°C, Condición: {condition}")
    #print(json.dumps(pronostico, indent=4))
else:
    print(' Error - Argumentos incorrectos'.center(100,'-'))
    print('Suministrar ciudad  - Ej: ./weather.py córdoba')
