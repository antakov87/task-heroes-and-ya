import requests

heroes = ["Hulk", "Captain America", "Thanos"]
TOKEN = '2619421814940190'
url = "https://superheroapi.com/api/2619421814940190/"

max_int = 0
max_hero = ''

for name in heroes:
    res = requests.get(url + "search/" + name)
    i = int(res.json()["results"][0]["powerstats"]["intelligence"])
    if i > max_int:
        max_hero = name
        max_int = i

print(max_hero)


