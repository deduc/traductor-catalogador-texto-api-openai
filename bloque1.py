from dotenv import load_dotenv
import requests
import json
import os


def guardar_respuesta_en_fichero(nombre_fichero, texto_json):
    with open(nombre_fichero, "a+", encoding="utf-8") as fi:
        json.dump(texto_json, fi, ensure_ascii=False, indent=4)
        fi.write("\n")


def peticion_http_api_completions(header, data, url):
    respuesta: requests.Response = requests.post(url, headers=header, json=data)
    return respuesta


def main_bloque_1(header, data):
    # header = {
    #     "Authorization": f"Bearer {API_KEY}",
    #     "Content-Type": "application/json"
    # }
    # data = {
    #     "model": f"{MODELO_IA}",
    #     "messages": [
    #         {"role": "system", "content": CONTEXTO_INICIAL},
    #         {"role": "assistant", "content": EJEMPLO_RESPUESTA_ASSISTANT},
    #         {"role": "user", "content": TEXTO_INICIAL_USER + TEXTO_IDIOMAS_USER},
    #     ],
    # }

    load_dotenv()

    TEXTO_INICIAL_USER = os.environ.get("TEXTO_INICIAL_USER")
    TEXTO_IDIOMAS_USER = os.environ.get("TEXTO_IDIOMAS_USER")
    API_COMPLETIONS_URL = os.environ.get("API_COMPLETIONS_URL")

    # Obtengo la respuesta y la formateo en json
    respuesta = peticion_http_api_completions(header, data, API_COMPLETIONS_URL).json()

    # Almaceno este nuevo atributo en el json obtenido
    respuesta["texto_entrada"] = TEXTO_INICIAL_USER + TEXTO_IDIOMAS_USER
    print(respuesta["choices"][0]["message"]["content"])

    guardar_respuesta_en_fichero(nombre_fichero="bloque_1.txt", texto_json=respuesta)