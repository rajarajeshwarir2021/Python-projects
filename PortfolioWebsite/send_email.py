import os
import smtplib, ssl


def send_email(receiver_email, message):
    host = "smtp.gmail.com"
    port = 465

    username = "raji.projects.101@gmail.com"
    password = os.getenv("PASSWORD")

    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)