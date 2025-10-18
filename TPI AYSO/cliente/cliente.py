import requests

URL = "http://servidor:5000"

response = requests.get(URL)

print("Servidor está ativo: ", response.json())