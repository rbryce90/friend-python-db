import requests 
# import webbrowser

url = 'https://dummyjson.com/todos'
data = requests.get(url).json()['todos']

for item in data: 
    del item['userId']
    print(item)
    # another request ot another service 
