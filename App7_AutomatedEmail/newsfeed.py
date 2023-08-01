import requests


class NewsFeed:
    """Representing multiple news titles and links as s single string"""

    base_url = "http://newsapi.org/v2/everything?"
    api_key = ""

    def __init__(self, interest, from_date, to_date, language="en"):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        """Gets the news"""
        url = self._build_url()
        articles = self._get_articles(url)
        email_body = self._build_email_body(articles)

        return email_body

    def _build_email_body(self, articles):
        email_body = ""
        for article in articles:
            email_body = email_body + article["title"] + "\n" + articles["url"] + "\n\n"
        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content["articles"]
        return articles

    def _build_url(self):
        url = f"{self.base_url}qInTitle={self.interest}&from={self.from_date}&to={self.to_date}&language={self.language}&apiKey={self.api_key}"
        return url