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
    top_5_global = []
    playlist_id = "34NbomaTu7YuOYnky8nLXL"  
    url_1 = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"    # Solicitar las pistas de la playlist
    lista = requests.get(url_1, headers=acceso)
    
    # Parsear la respuesta JSON
    playlist = lista.json()
    print(playlist)
    
        

else:
    print("Error al obtener el token de acceso:", respuesta.status_code)
