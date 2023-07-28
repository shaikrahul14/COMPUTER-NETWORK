import socket
import random
import string
import time
import sys
from threading import Thread

#=================================================================================
Buffersize = 1024
list_send_time = []

list_recv_timestamp = []

IP = "127.0.0.1"

PORT = 4578
print(f"Internet_protocal: {IP}")
print(f"port: {PORT}")

all_msgs = int(sys.argv[1])
time_interval = int(sys.argv[2]) 
size_of_packet = int(sys.argv[3])


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def sent_packets():
    for i in range(all_msgs):
        content_message = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=size_of_packet)).encode("utf-8")
        udp_socket.sendto(content_message, (IP, PORT))
        t1 = time.time()
        list_send_time.append(t1)
        print(f"message no:{i+1} sent. message:{content_message.decode('utf-8')}")
        time.sleep(time_interval)


def reciving_packets(): 
    c = 0
    while True:
        content_message, _ = udp_socket.recvfrom(Buffersize)
        if content_message:
            time_2 = time.time() 
            list_recv_timestamp.append(time_2) 
            print(f"message no:{c+1} received, message: {content_message.decode('utf-8')}")
            c += 1


if __name__ == "__main__":
    first_thread = Thread(target=sent_packets, daemon=True)
    second_thread = Thread(target=reciving_packets, daemon=True)
    first_thread.start()
    second_thread.start()
    while(True):
        
        if len(list_recv_timestamp) == all_msgs:
            
            print('RoundTripTime')
            m=(len(list_recv_timestamp)-all_msgs)/all_msgs *100 
            print(f'loss percentage={m}') 
            for i in range(all_msgs):
            
                print(
                    f'The Round TrIP Time for message{i+1}: {list_recv_timestamp[i]-list_send_time[i]}')
            
            break
