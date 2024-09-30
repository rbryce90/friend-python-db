import requests 
import webbrowser

for x in range(10):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    url = r.json()[0]['url']
    webbrowser.open(url)
