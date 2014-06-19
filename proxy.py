"""
Stupid simple UDP listener
"""
import socket
import sys


def listen(addr, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((addr, port))

    while True:
        yield sock.recvfrom(4096)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage: proxy.py <address> <port>'

    address = sys.argv[1]
    port = int(sys.argv[2])

    for (data, sender) in listen(address, port):
        print 'recv from {}: {}'.format(sender, data)
