# REST API
# json, xml
# GET, POST, PUT/PATCH, DELETE, HEAD
import requests

# pip install requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
print(response)  # <Response [200]>
# 200 ok
# 3xx - warningi, przekierowanie
# 4xx 404 - brak strony, 400 Bad Request błedne dane
# 5xx - błędy po stronie serwera %00 Internal Server Error
# https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP

print(response.text)

# zamiana na słownik
data = response.json()
print(data)
print(type(data))

for i in data:
    print(i)
# categories
# created_at
# icon_url
# id
# updated_at
# url
# value

print(data['value'])
# Chuck Norris once wrote a poem so beautiful, it makes menopausal women explode in their pants, and grown men sob awesomeness.

# "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
icon_url = data['icon_url']
response_img = requests.get(icon_url)

with open('icon.png', "wb") as f:  # wb - zapis abajtowy
    f.write(response_img.content)

print("Zdjęcie zostało zapisane")
