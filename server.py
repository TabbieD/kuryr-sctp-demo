#!/usr/bin/env python3

import socket
import platform
import sctp

# host = '10.0.1.105'
# port = 36412
host = '0.0.0.0'
port = 9090

sock = sctp.sctpsocket_tcp(socket.AF_INET)
sock.bind((host, port))
sock.listen(1)

while True:  
    # wait for a connection
    # print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        # show who connected to us
        # print('connection from', client_address)
        # print(connection)
        # receive the data in small chunks and print it
        while True:
            data = connection.recv(1024)
            if data:
                # output received data
                # print("Data: %s" % data)
                response = '%s: HELLO, I AM ALIVE!!!' % platform.node()
                sent = connection.send(response.encode('utf-8'))
            else:
                # no more data -- quit the loop
                # print("no more data.")
                break
    finally:
        # Clean up the connection
        connection.close()   
