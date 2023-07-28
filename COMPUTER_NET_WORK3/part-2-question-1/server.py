import socket
import time
IP = "127.0.0.1"
Port = 4578
BufferSize = 1024

try:
    
    udp_socket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_DGRAM)
  
    udp_socket.bind((IP, Port))
    print("udp server is created and listening")
except:
    print("Error occured socket not created")




while(True):
    client_msg, client_add = udp_socket.recvfrom(BufferSize)
    if client_msg:
        
        cMsg = client_msg.decode('utf-8')
        client_IP = client_add
        print("message:",cMsg, "Ip:", client_IP)
       
        time.sleep(1.5)
       
        udp_socket.sendto(client_msg, client_add)
        
