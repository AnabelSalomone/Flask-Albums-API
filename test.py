import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "album", {"name": "Little creatures", "year": 1986})
print(response.json())