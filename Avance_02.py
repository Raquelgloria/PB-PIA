import requests, re

def datos_artistas (coachella, i):
    for dia in coachella:
        for artista in dia:
            url_artista = f"https://api.spotify.com/v1/artists/{artista}"

            try:
                datos = requests.get(url_artista,headers = acceso)
                datos.raise_for_status()
                #Extracción de datos
                info = datos.json()
                #Verificación de datos
                #Los seguidores y popularidad son datos de tipo entero, por lo que no se necesitan verificar
                if len(info["genres"]) == 0:
                    info["genres"] = "desconocido"
                patron_id = re.compile(r'\w+')
                mo1 = re.match(patron_id, info["id"])
                if not mo1:
                    print(f"Error con el artista: {info["name"]} en su id")
                #Limpieza de datos
                artista = {
                    "nombre": info["name"],
                    "id": info["id"],
                    "generos": info["genres"],
                    "seguidores": info["followers"]["total"],
                    "popularidad": info["popularity"]}
                #print(artista)
                #Guardar datos
                informacion = datos_coachella[i]
                informacion.append(artista)
                    
            except requests.exceptions.ConnectionError:
                print("Error : no se pudo conectar a la API. verificar conexion y token")
        i += 1
    return informacion

#Información de acceso a la API
id_cliente = "c1728a05bf6f4890b21a083e89f4595e"
cliente_secreto = "aa03393bf46049a3bdddedd55f5786a0"
url = "https://accounts.spotify.com/api/token"
datos = {
    "grant_type": "client_credentials",
    "client_id": id_cliente,
    "client_secret": cliente_secreto}
encabezados = {"Content-Type": "application/x-www-form-urlencoded",}

respuesta = requests.post(url,data = datos, headers = encabezados)

#Datos de entrada
dia1 = ["1HY2Jd0NmPuamShAr6KMms","2wIVse2owClT7go1WT98tk", "22wbnEMDvgVIAGdFeek6ET",
        "2sSGPbdZJkaSE2AbcGOACx", "5L1lO4eRHmJ7a0Q6csE5cT", "4k1ELeJKT1ISyDv8JivPpB",
        "3oKRxpszQKUjjaHz388fVA", "6nB0iY1cjSY1KyhYyuIIKH", "0YinUQ50QDB7ZxSCLyQ40k",
        "0w1sbtZVQoK6GzV4A4OkCv", "2qoQgPAilErOKCwE2Y8wOG", "3qiHUAX7zY4Qnjx8TNUzVx",
        "2mG8HHQ9S9kcbjcrb5N1FE", "6CwfuxIqcltXDGjfZsMd9A", "5p9HO3XC5P3BLxJs5Mtrhm",
        "3SozjO3Lat463tQICI9LcE", "7eILArMiTFTQf8SEh5fFHK", "0oK5D6uPhGu4Jk2dbZfodU",
        "5y8tKLUfMvliMe8IKamR32", "0PCCGZ0wGLizHt2KZ7hhA2", "4l1cKWYW591xnwEGxpUg3J",
        "26s8LSolLfCIY88ysQbIuT", "7tm9Tuc70geXOOyKhtZHIj", "0H39MdGGX6dbnnQPt6NQkZ",
        "5fi7lIgJGH3RgUpJYcffQ7", "28uJnu5EsrGml2tBd7y8ts", "4v6XOdonnfpdTKTRJArG7v",
        "7zrkALJ9ayRjzysp4QYoEg", "3XxNRirzbjfLdDli06zMaB", "335TWGWGFan4vaacJzSiU8",
        "6I8TDGeUmmLom8auKPzMdX", "3BxjasMelf9pKaE4f7Y0So", "3EIJ8wiUHbgkRCt5cpRrQv",
        "3VNzWLePg9jTvQ2ximYOzW", "43UmVQp9qZILibJ5vHq21k", "67FB4n52MgexGQIG8s0yUH",
        "5EmEZjq8eHEC6qFnT63Lza", "4wf6GGNBqaU79839E6yjfn", "1GQur7dDvAWhKT9u9YwBJZ",
        "6L71LxY17w8Yzh1zUphpiW", "5RTLRtXjbXI2lSXc6jxlAz", "1jgSqmZTBltb5O2L7ErmEP",
        "2SdK1QDmZIP2hk94rSaLl9", "1ga48mxYYI9RuUrWLa3voh", "1UJfZU4rQx3bJ3tGypRuAT",
        "6n1t55WMsSIUFHrAL4mUsB", "4jercY4pUhY6jB8eQjpVJV", "1ZVACPeq7ccGCoUXwtafUU",
        "4Siyzg8kWayQfPQsPSl6JI", "4417xRt2a90h8KtmfsaWL8", "2Au9zIICTEr0oeV1iQrJ6X",
        "3cIXmCH7iNcslTbwrwS7zy", "0Adbm5kzcPUxFybf9fhjgG", "3eimPofmo9TuKJTgpM9Bcj",
        "0UKrJ4XldrkShYFCjRPhVa", "0Y5tJX1MQlPlqiwlOH1tJY"]
dia2 = ["7oPftvlwr6VrsViSDV7fJY", "25uiPmTg16RbhZWAqwLBy5", "1cXi8ALPQCBHZbf0EgP4Ey",
        "26WKgv73kRHD0gEDKD1i8j", "10gzBoINW3cLJfZUka8Zoe", "6PH3FLQAxtqYy46Zv08bpV",
        "3l0CmX0FuQjFxr8SK7Vqag", "5t5FqBwTcgKTaWmfEbwQY9", "4tYSBptyGeVyZsk8JC4JHZ",
        "3aQeKQSyrW4qWr35idm0cy", "4nVa6XlBFlIkF6msW57PHp", "6zlR5ttMfMNmwf2lecU9Cc",
        "7MoIc5s9KXolCBH1fy9kkw", "6Lt6KFXX3P0v6vfrynQAMo", "2933wDUojoQmvqSdTAE5NB",
        "5lVNSw2GPci8kebrAQpZqU", "0cxXnDhpgxcMMkKddhORHY", "3Ayl7mCk0nScecqOzvNp6s",
        "2nAKP6etu8wXNnezKXgqgg", "5Kmr0b3ip8g9P2i0dLTC3Z", "5isqImG0rLfAgBJSPMEVXF",
        "5Ho1vKl1Uz8bJlk4vbmvmf", "0NGAZxHanS9e0iNHpR8f2W", "5FzSQmddi3XVt5zuvfGStF",
        "1LTFJvVvRw7ghAyThxYmnF", "2mqiqsaX4LzFnUP7PmHGAb", "72NhFAGG5Pt91VbheJeEPG",
        "48LWLoeY0dhwaiX1FRsn72", "6htWLP8aiuf19FYMA4VQAZ", "6H77vD9YyhyxHBTkRpbMBk",
        "1np8xozf7ATJZDi9JX8Dx5", "0auP293abZeTWwMUi3fZw2", "6BV37tKh6pY97mnNdTCzly",
        "3C6wmSgnZuqxVQyBWujBsn", "7HfUJxeVTgrvhk0eWHFzV7", "0NSnLQRiWg2ZgnfrXaQ9P2",
        "0JXc5G7ZImFTwPg3y8MTfR", "6S2tas4z6DyIklBajDqJxI", "2AbQwU2cuEGfD465wCXlg2",
        "7mC3RkNNTV6p2j9w4F8Ip4", "7feJmqQ32fTIPKBmPXwHXf", "0pkLgeB9j465x1QB2kRoy4",
        "1H6X7yhnXZg73f9bssaj1Q", "29q1axQPERERxUzqufXMqB", "6XgIk9Y6qy6JCMZVime6DQ",
        "7zsy26T28IR0WxwVRZ9Aai", "4wNQV7tJw5nfk1xDAohIZg", "0Y5tJX1MQlPlqiwlOH1tJY"]
dia3 = ["246dkjvS1zLTtiykXe5h60", "181bsRPaVXVlUKXrxwZfHK", "2qxJFvFYMEDqd7ui6kSAcq",
        "7Gi6gjaWy3DxyilpF1a8Is", "250b0Wlc5Vk0CoUsaCY84M", "0dmPX6ovclgOy8WWJaFEUU",
        "35l9BRT7MXmM8bv2WDQiyB", "45yEuthJ9yq1rNXAOpBnqM", "0LOK81e9H5lr61HlGGHqwA",
        "4YrKBkKSVeqDamzBPWVnSJ", "3pc0bOVB5whxmD50W79wwO", "3jNkaOXasoc7RsxdchvEVq",
        "4iMO20EPodreIaEl8qW66y", "1GuqTQbuixFHD6eBkFwVcb", "2yLzlEFtIS0Q9UkyBZdQA7",
        "4SQdUpG4f7UbkJG3cJ2Iyj", "46pWGuE3dSwY3bMMXGBvVS", "3y2cIKLjiOlp1Np37WiUdH",
        "7c0XG5cIJTrrAgEC3ULPiq", "4ubY8RYfXkcEqgjEMDuLYl", "5tDjiBYUsTqzd0RkTZxK7u",
        "3NqV2DJoAWsjl787bWaHW7", "6caPJFLv1wesmM7gwK1ACy", "6RsLLSkSTcL4YrvgRcBTQd",
        "3wc57nV2fGEoM8x4xPK1O9", "7tjVFCxJdwT4NdrTmjyjQ6", "21UPYSRWFKwtqvSAnFnSvS",
        "6qxpnaukVayrQn6ViNvu9I", "6TsAG8Ve1icEC8ydeHm3C8", "3UtzOHYm3lQALkKzVD4wyO",
        "6uJ51uV5rYzu1MJkC4CceI", "27mWOSZjlpmtoqsRjRwQyu", "0zo109NM3S7CqHpvlXwqEN",
        "6ws5XBA70XgeBpnLZhQBoy", "3TJZG17pjOKXwx1ELKJPfm", "1z5xbcOeFRQXBVDpvRPh8H",
        "44qAhQu52dYKcHOFQd3esf", "74CcYmmNeHKe5PrZaISk8e", "3c1sTwL4HuWkrciiKHpnmx",
        "4UAW69682T7N0wrABUhqx0", "1txb9Qg5lJ3KATxPcIYyvO", "3xByNj8XW17oW0wsJhgzYL",
        "4CflzQprp6nZxKiv0t78tH", "1fRv9jiRIN7zAOSpOfRP73", "31UoyJXnXTjUzdwSX1Ylg5",
        "6TZbLCcOCv1DJvN28x3FBa", "18JlbX3l0yzlwdnQVJrLsp", "3RUNl0j2ISAQdC2Fxhj2q3", 
        "0Y5tJX1MQlPlqiwlOH1tJY"]
coachella = [dia1, dia2, dia3]

#Datos de salida
datos_dia1 = []
datos_dia2 = []
datos_dia3 = []
datos_coachella = [datos_dia1, datos_dia2, datos_dia3]

#Código principal    
if respuesta.status_code == 200:
    token = respuesta.json()["access_token"]
    #print("Token obtenido:", token)
    acceso = {"Authorization": "Bearer " + token}
    datos_artistas(coachella, 0)
else:
    print("Error al obtener el token de acceso:", respuesta.status_code)

#print(datos_coachella)
