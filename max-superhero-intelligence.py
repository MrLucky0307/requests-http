import requests


def superhero_intelligence(superhero_name):
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    for superhero in response.json():
        if superhero['name'] == superhero_name:
            return superhero['powerstats']['intelligence']


def max_superhero_intelligence(superheroes):
    max_intelligence = superheroes.get(max(superheroes))
    for hero, intelligence in superheroes.items():
        if intelligence == max_intelligence:
            print(f'Самый умный супергерой: {hero}')


superheros_intelligence = {'Hulk': superhero_intelligence('Hulk'),
                           'Captain America': superhero_intelligence('Captain America'),
                           'Thanos': superhero_intelligence('Thanos')}

max_superhero_intelligence(superheros_intelligence)
