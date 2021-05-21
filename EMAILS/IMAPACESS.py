import imaplib
import email
import getpass

imap_server = "imap.gmail.com"
imap_port = "993"


def check_email(username, password):
    m = imaplib.IMAP4_SSL(imap_server, imap_port)
    m.login(username, password)
    m.select("Inbox")
    result, data = m.uid("search", "FROM", "flipkart")
    
    for num in data[0].split():
        result, data = m.uid("fetch", num, "(RFC822)")
        email_message = email.message_from_bytes(data[0][1])
        print("From: " + email_message["From"])
        print("Subject: " + email_message["Subject"])
        break
    m.close()
    m.logout()


if __name__ == "__main__":
    username = input("Enter user: ")
    password = getpass.getpass(prompt="Enter password: ")
    check_email(username, password)
