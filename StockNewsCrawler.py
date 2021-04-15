import requests


for name in names:
    print(greet(name))

r = requests.get("https://google.com")
print(r.status_code)
