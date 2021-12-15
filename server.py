import socket
import sys
import logging

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
logging.basicConfig(filename='server.log', encoding='utf-8', level=logging.DEBUG,format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
logging.info( 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    logging.info('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        logging.info(sys.stderr, 'connection from',client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            logging.info('received "%s"' % data)
            if data:
                logging.info( 'sending data back to the client')
                connection.sendall(data)
            else:
                logging.info('no more data from', client_address)
                break
            
    finally:
        connection.close()