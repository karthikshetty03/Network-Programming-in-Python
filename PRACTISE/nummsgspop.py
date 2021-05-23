import getpass, poplib, sys


def main():
    hostname = 'pop.googlemail.com'
    username = 'karthikshetty03@gmail.com'
    passwd = getpass.getpass()
    p = poplib.POP3_SSL(hostname)  
    try:
        p.user(username)
        p.pass_(passwd)
    except poplib.error_proto as e:
        print("Login failed:", e)
    else:
        status = p.stat()
        # print(status)
        print("You have %d messages totaling %d bytes" % status)
        numMessages = len(p.list()[1])
        for i in range(0, 2):
            for j in p.retr(i+1)[1]:
                print(j.decode('utf-8'))
    finally:
        p.quit()


if __name__ == "__main__":
    main()
