import smtplib
import imghdr
from email.message import EmailMessage

SENDER = ""
APP_PASSWORD = ""
RECEIVER = ""


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as fh:
        content = fh.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail_server = smtplib.SMTP("smtp.gmail.com", 587)
    gmail_server.ehlo()
    gmail_server.starttls()
    gmail_server.login(SENDER, APP_PASSWORD)
    gmail_server.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail_server.quit()

    print("Email was sent!")