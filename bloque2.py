from dotenv import load_dotenv
import json
import os
import requests


def guardar_respuesta_en_fichero(nombre_fichero, texto_json):
    with open(nombre_fichero, "a+", encoding="utf-8") as fi:
        json.dump(texto_json, fi, ensure_ascii=False, indent=4)
        fi.write("\n")


def peticion_http_api_moderations(header, data, url):
    respuesta: requests.Response = requests.post(url, headers=header, json=data)
    return respuesta


def main_bloque_2(header, data):
    load_dotenv()
    API_MODERATIONS_URL = os.environ.get("API_MODERATIONS_URL")
    TEXTO_INICIAL_USER = os.environ.get("TEXTO_INICIAL_USER")

    respuesta = peticion_http_api_moderations(header, data).json()

    # Almaceno este nuevo atributo en el json obtenido
    respuesta["texto_entrada"] = TEXTO_INICIAL_USER

    print("Texto potencialmente dañino:", respuesta["results"][0]["flagged"], "\nTexto inicial:", TEXTO_INICIAL_USER)
    
    guardar_respuesta_en_fichero(nombre_fichero="bloque_2.txt", texto_json=respuesta)
