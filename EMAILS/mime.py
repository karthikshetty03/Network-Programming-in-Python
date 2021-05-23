from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg["To"] = "paresh@example.com"
msg["From"] = "npstudent@example.com"
msg["Subject"] = "Query regarding MIME"
from email.mime.text import MIMEText

part = MIMEText("text", "plain")
message = "Please explain MIME again in the next class"
part.set_payload(message)
msg.attach(part)
msg.as_string()
print(msg)
