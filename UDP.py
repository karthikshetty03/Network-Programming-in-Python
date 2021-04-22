import socket, argparse
from datetime import datetime

MAX_BYTES = 6555


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('Server starts istening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client at {} says {}'.format(address, text))
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        sock.sendto(data, address)


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'The time at my side {}'.format(datetime.now())
    data = text.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print('The server at this {} location replied {!r}'.format(address, text))


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(
        description='send and recieve udp locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p',
                        metavar='PORT',
                        type=int,
                        default=1060,
                        help='default UDP port')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)