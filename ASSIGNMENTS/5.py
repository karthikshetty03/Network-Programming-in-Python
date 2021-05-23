
import imaplib, getpass, email

def read(username, password):
  mail = imaplib.IMAP4_SSL('imap.gmail.com')
  (retcode, capabilities) = mail.login(username, password)
  mail.list()
  mail.select('inbox')
  (retcode, messages) = mail.search(None, '(UNSEEN)')

  if retcode == 'OK':
    for num in messages[0].split():
        print('Processing... ')
        typ, data = mail.fetch(num,'(RFC822)')
        for response_part in data:
          if isinstance(response_part, tuple):
              original = email.message_from_string(response_part[1])
              print(original['From'])
              print(original['Subject'])
              # typ, data = mail.store(num,'+FLAGS','\\Seen')
  mail.close()
  mail.logout()

if __name__ == '__main__':
  username = input("ENter username: ")
  password = getpass.getpass(prompt = "Enter password: ")
  read(username, password)