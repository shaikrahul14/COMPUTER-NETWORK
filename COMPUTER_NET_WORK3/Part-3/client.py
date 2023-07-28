#importing required libraries
import socket 

print("choose any internet_protocol 1 or 2:")
internet_protocol = int(input("1 -> IPV4 \n2 -> IPV6 \nEnter the internet_protocol 1 or 2: ")) 
host = input("Hostname: ") 

print("give any port_number number which you like-")
p_number = int(input("Port number: "))  

if internet_protocol == 1:
    family = socket.AF_INET # default ipv4



else:
    family = socket.AF_INET6 # default  IPv6

#===========================================================================================================    

address = socket.getaddrinfo(host, p_number, family= family)

for i in range(len(address)):
    host = address[i][4][0]



    p = socket.socket(family=family, type=address[i][1])


    p.connect((host,p_number))



    p.close()
    break
        
family = address[i][0] 
type = address[i][1]
host = address[i][4][0]
#======================================================================================================




z= socket.socket(family= family, type= type) 
z.connect((host, p_number)) 
print("ENTER 'end' to stop close the connection!")


while True:
    coming_data = input("give the data to send: ")
    if coming_data == "end":
        break 





    z.send(str.encode(coming_data))
    out_data = z.recv(1024)
    print(out_data.decode()) 
z.close()
