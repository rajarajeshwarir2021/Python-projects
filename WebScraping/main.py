import time
import sqlite3
import requests
import selectorlib
import smtplib, ssl

REQUEST_URL = f"https://programmer100.pythonanywhere.com/tours/"

# Establish a connection and cursor
connection = sqlite3.connect("data.db")


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
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


def store(band, city, date):

    sql_cursor = connection.cursor()
    # Insert new data records
    sql_cursor.execute("INSERT INTO events VALUES(?,?,?)", (band, city, date))
    connection.commit()


def read(band, city, date):

    sql_cursor = connection.cursor()
    sql_cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = sql_cursor.fetchall()

    return rows


if __name__ == '__main__':
    while True:
        scraped = scrape(REQUEST_URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            band, city, date = extracted.split(', ')
            print(f"Band: {band}\nCity: {city}\nDate: {date}")

            rows = read(band, city, date)
            if not rows:
                store(band, city, date)
                #send_email(message="Hey, new event was found!")
        time.sleep(2)


