import getpass
import poplib

GOOGLE_POP3_SERVER = "pop.googlemail.com"
POP3_SERVER_PORT = "995"


def fetch_email(username, password):
    mailbox = poplib.POP3_SSL(GOOGLE_POP3_SERVER, POP3_SERVER_PORT)
    mailbox.user(username)
    mailbox.pass_(password)
    num_messages = len(mailbox.list()[1])
    print("Total Emails: {0}".format(num_messages))
    mailbox.quit()


if __name__ == "__main__":
    username = input("Enter your email: ")
    password = getpass.getpass(prompt="Enter password: ")
    fetch_email(username, password)
