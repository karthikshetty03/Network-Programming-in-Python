import socket, argparse


def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only recieved'
                           ' %d bytes before the socket closed' %
                           (length, len(data)))
        data += more
    return data


def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.listen(1)
    print('Server starts listening at {}'.format(sock.getsockname()))
    while True:
        sc, sockname = sock.accept()
        print('We have recieved the connection from ', sockname)
        print('Sock Name :', sc.getsockname())
        print('Peer name : ', sc.getpeername())
        message = recvall(sc, 44)
        print('Message recieved : ', repr(message))
        sc.sendall(b'Thank You ! Client')
        sc.close()
        print('The reply is sent to the client')


def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned the socket name', sock.getsockname())
    reply = b'Hi server! We are learning the TCP programme'
    sock.sendall(reply)
    reply = recvall(sock, 18)
    print('The server replied : ', repr(reply))
    sock.close()


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='trying to run tcp locally')
    parser.add_argument('role', choices=choices, help='select role to play')
    parser.add_argument('host',
                        help='interface the server listems at;'
                        ' host the client sends to')
    parser.add_argument('-p',
                        metavar='PORT',
                        type=int,
                        default=1060,
                        help='specify port')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
