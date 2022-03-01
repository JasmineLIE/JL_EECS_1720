'''
Much like server, uses the same socket, but instead of binding we connect
'''

import socket #already comes installed

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2000)) #can communicate to and from Python programs on the same machine, on local network set of machines, or remote network

while True:
    msg = s.recv(8) #rhis is the buffer; TCP socket is a stream of data.  Have to decide how big of chunks of data do we want to receive at a time.  IN this case 1024

    print(msg.decode("utf-8")) #communicating via byte-stream.  Receive bytes, read bytes then decode bytes

'''
Now run on command prompt
'''