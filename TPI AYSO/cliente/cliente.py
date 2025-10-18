import requests

URL = "http://localhost:5000"

response = requests.get(URL)

print("Servidor está ativo:", response.json())