'''
Much like server, uses the same socket, but instead of binding we connect
'''


import socket #already comes installed

HEADERSIZE = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2000)) #can communicate to and from Python programs on the same machine, on local network set of machines, or remote network

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("utf=8")

        if len(full_msg) -HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = '' #empty it out

'''

Now run on command prompt
'''