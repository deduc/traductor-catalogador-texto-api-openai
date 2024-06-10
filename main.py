from dotenv import load_dotenv
from bloque1 import main_bloque_1
from bloque2 import main_bloque_2
import os



def main():
    load_dotenv()

    API_KEY = os.environ.get("API_KEY")
    MODELO_IA = os.environ.get("MODELO_IA")
    CONTEXTO_INICIAL = os.environ.get("CONTEXTO_INICIAL")
    EJEMPLO_RESPUESTA_ASSISTANT = os.environ.get("EJEMPLO_RESPUESTA_ASSISTANT")
    TEXTO_INICIAL_USER = os.environ.get("TEXTO_INICIAL_USER")
    TEXTO_IDIOMAS_USER = os.environ.get("TEXTO_IDIOMAS_USER")
    
    # Creo los argumentos para la llamada http del primer bloque
    header = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": f"{MODELO_IA}",
        "messages": [
            {"role": "system", "content": CONTEXTO_INICIAL},
            {"role": "assistant", "content": EJEMPLO_RESPUESTA_ASSISTANT},
            {"role": "user", "content": TEXTO_INICIAL_USER + TEXTO_IDIOMAS_USER},
        ],
    }


    main_bloque_1(header, data)

    # Creo los argumentos para la llamada http del segundo bloque
    header = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "input": [TEXTO_INICIAL_USER]
    }

    main_bloque_2(header, data)


main()