# An example script to connect to Google using socket
# programming in Python
import socket # for socket
import sys
import time
import logging

#Setting next one second
logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG,format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
t_end = time.time() + 1


imsi=999980000000000

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	logging.info("Socket successfully created")
except socket.error as err:
	logging.info("socket creation failed with error %s" %(err))

# default port for socket
port = 25050
#port=10000

try:
	host_ip = socket.gethostbyname('10.0.14.116')
except socket.gaierror:

	# this means could not resolve the host
	logging.info("there was an error resolving the host")
	sys.exit()

# connecting to the server
s.connect((host_ip, port))

logging.info("the socket has successfully connected to the Server")

try:    
    # Send data
    c=0
    a=time.perf_counter()
    while True:
        if(imsi<999980000014999):
            imsi=imsi+1
            c=c+1
            if(time.time() < t_end):
                if(c<1500):
                    message = f'20211113184359,UL,MAP,327700040900301,327700040900301,SUCCESS,VLR,327700040900301,INDSC,203,327700040900301,327700040900301\n'
                    #message = f'20211113184359,CL,MAP,328800000044216,887711000019216,SUCCESS,VLR,324750007339015,INDSC,203,41650599,887711000019216\n'
                    logging.info(f'sending {message}')
                    s.send(message.encode("utf-8"))
                    logging.info('Message Sent"%s"' % c) 
                    break;                    
                else:
                    b=time.perf_counter()
                    d=a-b;
                    logging.info('total time taken"%s"' %d)
                    break
            else:
                b=time.perf_counter()
                d=a-b;
                logging.info('total time taken"%s"' %d)
                time.sleep(5)
                break
finally:
    logging.info('closing socket')
    s.close()
s