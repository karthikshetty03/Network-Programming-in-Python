from email.mime.nonmultipart import MIMENonMultipart
import getpass
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTYP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def send_email(sender, recipient):
    msg = MIMEMultipart()
    msg["To"] = recipient
    msg["From"] = sender
    msg["Subject"] = input("Enter your email Subject: ")
    message = input("Enter your message: ")
    part = MIMEText("text", "plain")
    part.set_payload(message)
    msg.attach(part)

    session = smtplib.SMTP(SMTYP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
    password = getpass.getpass(prompt="Enter your password: ")
    session.login(sender, password)
    session.sendmail(sender, recipient, msg.as_string())
    print("Your email has been sent to {0}".format(recipient))
    session.quit()


if __name__ == "__main__":
    sender = input("Enter sender email: ")
    recipient = input("Enter recipient email: ")
    send_email(sender, recipient)
