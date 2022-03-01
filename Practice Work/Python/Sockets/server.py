import socket #already comes installed

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #declaring the family type, which is AF_INET -- SOCK_STREAM is a streaming socket
s.bind((socket.gethostname(), 2000)) #lower digits already occupied by some other program
s.listen(5) #prepare server to listen and leave queue of 5 when messages start stacking up

while True:
    clientsocket, address = s.accept()
    #anybody connects and then we store client socket object into the clientsocket and address where they're coming from
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8")) #sending information and what type of bytes
    #send information to the clientsocket

'''
What is a Socket?

A socket is the endpoint -- gonna have two end points for communication -- that receives data.  Sends and receives data.  

The socket itself is not the communication, it's the end point that receives the communication and sits at an IP in a port 

To run it using CMD, find the folder location and type cmd in the address bar
'''