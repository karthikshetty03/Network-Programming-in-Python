import socket, argparse, random, time
from datetime import datetime

tasks = {
    b"beautiful is better than?": b"Ugly.",
    b"Explcit is better than?": b"Implcit.",
    b"Which is this network programming session?": b"2020-21.",
}


def client(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    for task in random.sample(list(tasks), 3):
        #print(task)
        sock.sendall(task)
        print(recv_until(sock, b"."))
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("current time = ", current_time)
    sock.close()


def recv_until(sock, suffix):
    """Recieve bytes over socket 'spck' until we recieve the suffix"""
    message = sock.recv(4096)
    if not message:
        raise EOFError("socket closed")
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise IOError("recieved {!r} then socket closed".format(message))
        message += data
    return message


def parse_command_line(description):
    parser = argparse.ArgumentParser(description="Example Client")
    parser.add_argument('host', help="IP or hostname")
    #parser.add_argument('-e', action="store_true", help="cause an error")
    parser.add_argument('-p',
                        metavar="port",
                        type=int,
                        default=1060,
                        help="TCP port (default is 1060)")
    args = parser.parse_args()
    address = (args.host, args.p)
    return address


if __name__ == "__main__":
    address = parse_command_line("simple client")
    client(address)
