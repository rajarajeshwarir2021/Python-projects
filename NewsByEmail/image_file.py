import requests

request_url = "https://en.wikipedia.org/wiki/Dog#/media/File:Wilde_huendin_am_stillen.jpg"

response = requests.get(request_url)

with open("image.jpg", "wb") as fh:
    fh.write(response.content)