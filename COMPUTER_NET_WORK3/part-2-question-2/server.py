import socket #importing the socket module
import time
IP = "127.0.0.1" #localhost ipv4 addr_essess 
port_no = 5048 # port number = 5048
Buffer_size = 1024 # buffersize inializing

try:
    soc_ket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    soc_ket.bind((IP, port_no))
    print("udp sever is ready and listening")
except:
    print(" Socket creating error")


while(True):
    message, addr_ess = soc_ket.recvfrom(Buffer_size) #data packets receive from client
    if message:
        soc_ket.sendto(message, addr_ess)
        #data packets sending to client
