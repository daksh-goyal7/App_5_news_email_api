import requests
from send_mail import send_email
topic="tesla"

api_key="9d90f944f0a641f2ae7be99407bdfde5"
url="https://newsapi.org/v2/everything?" \
     f"q={topic}&" \
     "from=2023-10-11&" \
     "sortBy=publishedAt&" \
     "apiKey=9d90f944f0a641f2ae7be99407bdfde5&" \
     "language=en"
request=requests.get(url)
content=request.json()
body=""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body=body+article["title"]+"\n"+article["description"]+"\n"+article["url"]+2*"\n"
body="Subject: Daksh's Tesla Podcast"+"\n" \
     + body
body=body.encode("utf-8")
send_email(body)
