import socket
import os
import sctp
import sys

sk = sctp.sctpsocket_tcp(socket.AF_INET)
# sk.connect(("127.0.0.1", int(9090)))


def connect_plus_message(OUT_IP, OUT_PORT):
    sk.connect((OUT_IP, OUT_PORT))
    print("Sending Message")
    sk.sctp_send(msg='HELLO, I AM ALIVE!!!')
    msgFromServer = sk.recvfrom(1024)
    print(msgFromServer[0].decode('utf-8'))
    sk.shutdown(0)
    sk.close()


if __name__ == '__main__':
    connect_plus_message(sys.argv[1],int(sys.argv[2]))
