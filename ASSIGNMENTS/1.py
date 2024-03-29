import smtplib, getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "karthikshetty03@gmail.com"
you = "karthikshetty03@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart("alternative")
msg["Subject"] = "Comprehensive Exam 2021-22"
msg["From"] = me
msg["To"] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p><b>Hi! Welcome to Network Programming</b></p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
session = smtplib.SMTP("smtp.gmail.com")
session.ehlo()
session.starttls()
session.ehlo()
password = getpass.getpass(prompt="Enter your password: ")
session.login(me, password)
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
session.sendmail(me, you, msg.as_string())
session.quit()
