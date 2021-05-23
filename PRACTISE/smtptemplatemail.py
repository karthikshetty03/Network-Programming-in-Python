import sys, smtplib, getpass

message_template = """To: {}
From: {}
Subject: Test Message from simple.py
Hello,
This is a test message sent to you from the simple.py program
in Foundations of Python Network Programming.
"""

SMTYP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def main(sender, recipient):
    session = smtplib.SMTP(SMTYP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
    password = getpass.getpass(prompt="Enter your password: ")
    session.login(sender, password)
    message = message_template.format(recipient, sender)
    session.sendmail(sender, recipient, message)
    print("Your email has been sent to {0}".format(recipient))
    session.quit()


if __name__ == "__main__":
    sender = input("Enter sender email: ")
    recipient = input("Enter recipient email: ")
    main(sender, recipient)
