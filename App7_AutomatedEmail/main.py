import pandas
import yagmail
import datetime
from newsfeed import NewsFeed
import time


def send_email():
    today = datetime.datetime.now().strftime("%y-%m-%d")
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%y-%m-%d")
    news_feed = NewsFeed(interest=row['interest'], from_date=yesterday, to_date=today)
    email = yagmail.SMTP(user="xxx@gmail.com", password="xxxxx")
    email.send(to=row["email"],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\n See what's on about {row['interest']} today.\n {news_feed.get()}\nRaji")


if __name__ == '__main__':

    while True:
        if datetime.datetime.now().hour == 8 and datetime.datetime.now().minute == 00:
            df = pandas.read_excel("files/people.xlsx")

            for index, row in df.iterrows():
                send_email()

            time.sleep(60)