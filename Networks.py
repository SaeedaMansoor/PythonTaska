
import socket
# in order toconnect to the internet you need a port or an end connection
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM); # THIS WILL MAKE AN END PPORT
mysocket.connect(('data.pr4e.org',80)); # 80 is the port and string is the host


# Connecting to a server
# we use the GET COMMAND
#EXAMPLE
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd);   # request sent to the server for the connection establlishment


# now you can use the WHILE LOOP in orer to receive the files
while True:
    data=mysocket.recv(512);
    if (len(data)<1):  # means if we doont get data just break the loop
        break;
    else:
        print(data.decode()); # decoding the data
mysocket.close();  # closing the connection
