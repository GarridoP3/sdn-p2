import requests

url = "https://api.meraki.com/api/v1/organizations"

headers = {
    "Authorization": "Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6",
    "Accept": "application/json"
}

organizations = requests.request('GET', url, headers=headers)
excepcion = organizations.raise_for_status() #En caso de error, genera una excepción

print('¿Ocurrió un error?', excepcion)
print('Organizaciones: ', organizations.json())