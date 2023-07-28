import socket  
import sys   
import random  
import string 
import time  
#============================================================
Buffersize = 1024 
list_send_time= []  
list_recv_timestamp = [] 
Ip = "localhost" 
port_no = 5048 
if(len(sys.argv)!=3):
    print("arguments overflow error")
    exit(0)
x =[]
y_throughput =[]
y_average_delay =[]  
y_averagedelay = []  
#====================================================    
time_interval_len = int(sys.argv[1]) # first argument time interval argument
data_size = int(sys.argv[2]) #second argument packetsize 
sock_et = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #udp socket is ready
print("run the plot.plt to get the graphs")
def echoclientsoc():
    t=0
    count=0
    packet_send=0
    time_initialize=time.time()

#===============================================================================================    
    while True:
        if(t==time_interval_len):
            break
        msg_info = ''.join(random.choices(

            string.ascii_uppercase + string.digits, k=data_size)).encode("utf-8")
        sock_et.sendto(msg_info, (Ip, port_no))  #sending msg_info to server
        sent_time = time.time() 
        list_send_time.append(sent_time)
        msg_info, _ = sock_et.recvfrom(Buffersize)
        if msg_info:
            packet_recv_time = time.time()  #packet recived time calulating
            count+=packet_recv_time-sent_time
            packet_send+=1


            if(packet_recv_time-time_initialize>=1):
                time_initialize=time.time()

                round_trip_time=count/packet_send 
                count=0
                avg_delay=round_trip_time/2 
                t+=1
                print(t,(packet_send*data_size)/1000,avg_delay*1000,sep=", ") #printing the throushput and average delay
                x.append(t)
                y_throughput.append((packet_send*data_size)/1000)
                y_averagedelay.append(avg_delay*1000)
                packet_send=0
            list_recv_timestamp.append(packet_recv_time) 
        else:
            continue    
            
if __name__ == "__main__":
    echoclientsoc()


import matplotlib.pyplot as plt
plt.xlabel("time")
plt.ylabel("throughput ")
plt.plot(x,y_throughput)
plt.savefig("throput_graph.png")
plt.clf()
plt.xlabel("time")
plt.ylabel("averagewg delay ms")
plt.plot(x,y_averagedelay)

plt.savefig("average_delay_graph")