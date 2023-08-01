import time
import sqlite3
import requests
import selectorlib
import smtplib, ssl

REQUEST_URL = f"https://programmer100.pythonanywhere.com/tours/"


class Event:
    def __init__(self):
        self.source = None

    def scrape(self):
        """Scrape the page source from the URL"""
        response = requests.get(REQUEST_URL)
        self.source = response.text

    def extract(self):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(self.source)["tours"]
        return value


class Email:
    def send(message):
        host = "smtp.gmail.com"
        port = 465

        username = "YOUR_GMAIL_ID"
        password = "YOUR_GMAIL_APP_PASSWORD"

        receiver = "YOUR_GMAIL_ID"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("Email was sent!")


class Database:

    def __init__(self, extracted_data):
        self.band, self.city, self.date = extracted_data.split(', ')

        # Establish a connection and cursor
        self.connection = sqlite3.connect("data.db")

    def read(self):
        sql_cursor = self.connection.cursor()
        sql_cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (self.band, self.city, self.date))
        rows = sql_cursor.fetchall()

        return rows

    def store(self):
        sql_cursor = self.connection.cursor()
        # Insert new data records
        sql_cursor.execute("INSERT INTO events VALUES(?,?,?)", (self.band, self.city, self.date))
        self.connection.commit()

    def __str__(self):
        print(f"Band: {self.band}\nCity: {self.city}\nDate: {self.date}")


if __name__ == '__main__':
    while True:
        event = Event()
        event.scrape()
        extracted = event.extract()
        print(extracted)

        if extracted != "No upcoming tours":
            database = Database(extracted)
            rows = database.read()
            if not rows:
                database.store()
                #email = Email()
                #email.send(message="Hey, new event was found!")
        time.sleep(2)


