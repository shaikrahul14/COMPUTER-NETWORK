import socket
import os
import time
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def packet_send(link,frame):
    link.send(bytes(frame,"utf-8")) 
    print("==>>",frame)


def packet_recived(link):
    frame = link.recv(1024).decode()
    print("<<==",frame)
    return frame



def server_socket():
    IP = "localhost" # default localhost ipv4
    PORT = 5678      
    soc = socket.socket()
    soc.bind((IP, PORT)) # binding ip and port 
    soc.listen(10)
    print("tcp server ready and listing to client")
    while True:

        link , addr = soc.accept()
        print("Client Connected    :",addr)
        frame = packet_recived(link) 
        valid = os.path.exists(f"./server_folder/{frame}")

        if valid:
            with open(f"./server_folder/{frame}","r") as f:
                file_data = f.read().split(" ")
            packet_send(link,file_data[0])

            while True:
                frame = packet_recived(link)
                time.sleep(1)
                if frame == "BREAK":
                    packet_send(link,"BREAK")
                    break

                inde = int(frame.split("$")[1])

                packet_send(link,file_data[inde])
                if file_data[inde] == "EOF":
                    break


        else:
            packet_send(link,"404:File-not-Found")
        
        link.close()
        print("Client Disconnect and close :",addr)


if __name__ == '__main__':
    server_socket()