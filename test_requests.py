import requests

url = 'https://itunes.apple.com/search?/'

params = {
    'term': 'Сергей Шнуров',
    'limit': 200,
    }

response = requests.get(url, params)
print(response.json())