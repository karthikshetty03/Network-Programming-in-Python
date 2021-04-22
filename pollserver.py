import socket, argparse, time, select

tasks = {
    b"beautiful is better than?": b"Ugly.",
    b"Explcit is better than?": b"Implcit.",
    b"Which is this network programming session?": b"2020-21.",
}


def serve(listener):
    sockets = {listener.fileno(): listener}
    addresses = {}
    bytes_recieved = {}
    bytes_to_send = {}
    poll_object = select.poll()
    poll_object.register(listener, select.POLLIN)

    for fd, event in all_events_forever(poll_object):
        sock = sockets[fd]

        #server is recieving a new connection
        if sock is listener:
            sock, address = sock.accept()
            print('Accepted Connection from {}'.format(address))
            sock.setblocking(True)
            sockets[sock.fileno()] = sock
            addresses[sock] = address
            poll_object.register(sock, select.POLLIN)

        #socket is closed from the client side
        elif event & (select.POLLHUP | select.POLLERR | select.POLLNVAL):
            address = addresses.pop(sock)
            rb = bytes_recieved.pop(sock, b'')
            sb = bytes_to_send.pop(sock, b'')
            if rb:
                print(
                    'abnormal close, client {} sent {} but then closed'.format(
                        address, rb))
            elif sb:
                print('abnormal close, client {} closed before we sent'.format(
                    address, sb))
            else:
                print('normal closing of client {}'.format(address))
            poll_object.unregister(fd)
            del sockets[fd]

        #server ready to read from client
        elif event & select.POLLIN:
            more_data = sock.recv(4096)
            if not more_data:
                sock.close()
                continue
            data = bytes_recieved.pop(sock, b'') + more_data
            if data.endswith(b'?'):
                print(data)
                bytes_to_send[sock] = get_answer(data)
                poll_object.modify(sock, select.POLLOUT)
            else:
                bytes_recieved[sock] = data

        #server is ready to send to client
        elif event & select.POLLOUT:
            data = bytes_to_send.pop(sock)
            n = sock.send(data)
            if n < len(data):
                bytes_to_send[sock] = data[n:]
            else:
                poll_object.modify(sock, select.POLLIN)


def all_events_forever(poll_onject):
    while True:
        for fd, event in poll_onject.poll():
            yield fd, event


def create_srv_socket(address):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(address)
    listener.listen(64)
    print("Listening at {}".format(address))
    return listener


def accept_connections_forever(listener):
    while True:
        sock, address = listener.accept()
        print("Accepted connection from {}".format(address))
        handle_conversation(sock, address)


def handle_conversation(sock, address):
    try:
        while True:
            handle_request(sock)
    except EOFError:
        print("Client socket to {} has closed".format(address))
    except Exception as e:
        print("Client : {},  Error : {}".format(address, e))
    finally:
        sock.close()


def handle_request(sock):
    task = recv_until(sock, b'?')
    print(task)
    answer = get_answer(task)
    #print(answer)
    sock.sendall(answer)


def recv_until(sock, suffix):
    """Recieve bytes over socket 'sock' until we recieve the suffix"""
    message = sock.recv(4096)
    if not message:
        raise EOFError("socket closed")
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise IOError("recieved {!r} then socket closed".format(message))
        message += data
    return message


def get_answer(task):
    time.sleep(2)
    return tasks.get(task, b"task not in database !")


def parse_command_line(description):
    """Parse command line and return a socket address"""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("host", help="IP or host name")
    parser.add_argument("-p",
                        metavar="port",
                        type=int,
                        default=1060,
                        help="TCP port (default is 1060)")
    args = parser.parse_args()
    address = (args.host, args.p)
    return address


if __name__ == "__main__":
    address = parse_command_line("simple single threaded server")
    listener = create_srv_socket(address)
    serve(listener)
