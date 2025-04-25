import requests

id_cliente = "c1728a05bf6f4890b21a083e89f4595e"
cliente_secreto = "aa03393bf46049a3bdddedd55f5786a0"


url = "https://accounts.spotify.com/api/token"

datos = {
    "grant_type": "client_credentials",
    "client_id": id_cliente,
    "client_secret": cliente_secreto
}

encabezados = {
    "Content-Type": "application/x-www-form-urlencoded",
    
    
}

respuesta = requests.post(url,data = datos, headers = encabezados)

if respuesta.status_code == 200:
    token = respuesta.json()["access_token"]
    #print("Token obtenido:", token)
    
    acceso = {
        "Authorization": "Bearer " + token
    }
    
    artista_id = "5L1lO4eRHmJ7a0Q6csE5cT"  #LISA de BLACKPINK,se puede cambiar el id
    # Por motivo de prueba, se coloca el ID del artista directamente.
    # Sin embrago la API de Spotify cuenta con la url para poder buscar en nombre de artista.
    # sin necesidad de tener el ID, solo ingresando el nombre.
    url_1 = f"https://api.spotify.com/v1/artists/{artista_id}"

    try:
        datos = requests.get(url_1,headers = acceso)
        datos.raise_for_status()
        artistas = datos.json()
        artista = {
            "nombre": artistas["name"],
            "generos": artistas["genres"],
            "seguidores": artistas["followers"]["total"],
            "popularidad": artistas["popularity"],
            "url_spotify": artistas["external_urls"]["spotify"]
        }
        print(artista)
    except requests.exceptions.ConnectionError:
        print("Error : no se pudo conectar a la API. verificar conexion y token") 

else:
    print("Error al obtener el token de acceso:", respuesta.status_code)
