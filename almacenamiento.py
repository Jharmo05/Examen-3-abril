import json
import os


archivo_json = 'servicios_fotograficos.json'


def cargar_servicios():
    if os.path.exists(archivo_json):
        with open(archivo_json, 'r') as archivo:
            return json.load(archivo)
    else:
        return []


def guardar_servicios(servicios):
    with open(archivo_json, 'w') as archivo:
        json.dump(servicios, archivo, indent=4)




