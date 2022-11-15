import requests

def catchTracker():
    URL = "http://20.124.90.164/catch/tracker"
    respuesta = requests.get(url=URL)

    datos = respuesta.json()
    return datos