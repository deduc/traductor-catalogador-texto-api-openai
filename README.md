# Traductor universal

## Bloque 1
Funcion que genere y ejecute un prompt contra la API completions de OpenAI (https://api.openai.com/v1/chat/completions) que explique la tarea a realizar con estas premisas:
- La funcion recibe estos pakrametros:
    - Texto a traducir
    - Lista de idiomas a los que se quiere traducir el texto
- La salida del prompt debe identificar el idioma del texto introducido de la siguiente forma:
    - mensaje original (idioma):(issue)
- La salida del prompt debe obtener un listado con el siguiente formato:
    - idioma1: traduccion1
    - idioma2: traduccion2
    - . . .
    - idiomaN: traduccionN

## Bloque 2
Pasa el texto del issue a la API de moderacion (https://platform.openai.com/docs/api-reference/moderations) de openai y averigua e imprime si se etiqueta como verdadero (esto significa que el texto se ha clasificado como potencialmente dañino)
