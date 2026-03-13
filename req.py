import requests
while True:
    x = requests.get("http://localhost:8080/test")
    print(x.headers)
    print(x.content)
