import json
from send_email import send_email

import requests

topic = "tesla"
request_url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAtapiKey=890603a55bfa47048e4490069ebee18c&language=en"
api_key = "890603a55bfa47048e4490069ebee18c"

# Make request
response = requests.get(request_url)

# Get a dictionary with data
content = response.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + '\n' + body + article["title"] + '\n' + article["description"] + '\n' + article["url"] + 2*'\n'

body.encode("utf-8")
send_email(message=body)

