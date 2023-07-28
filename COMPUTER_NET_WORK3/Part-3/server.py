
import socket 

host = "" 
print("---give any port which you like")
port = int(input("Port number:")) 


soc=socket.socket(socket.AF_INET6, socket.SOCK_STREAM) 




soc.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)# The setsockopt() function provides an application program with the means to control socket behavior. An application program can use setsockopt() to allocate buffer space, control timeouts, or permit socket data broadcasts.
soc.bind((host, port)) 
soc.listen(3) 

while True:
    p, add = soc.accept() 



    if p:
        print('Connection established with ', add)
        while True:
            income_data = p.recv(1024) 
            
            
            
            
            
            
            if not income_data:
                break 
            p.send(income_data) 
