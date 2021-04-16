import requests


names = ["Paulina", "Tom", "Marlon"]


def greet(Nombre):
    print("Hello" + " " + Nombre)


for name in names:
    print(greet(name))

r = requests.get("https://google.com")
print(r.status_code)