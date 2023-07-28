import socket
import time
#===========================================================================
name_of_file = input("file name (file_1.txt) :")
if name_of_file == "":
    name_of_file = "file_1.txt"

def client():
    IP = "localhost" 
    PORT = 5678
    soc = socket.socket()
    soc.connect((IP, PORT))
    msg = name_of_file
    soc.send(msg.encode())
    recv_info = []
    while True:
        frame = soc.recv(1024).decode()
        time.sleep(2)
        if frame in ["404 file is not found"]:
            print(f"invalid file : File '{name_of_file}' not found")
            break
        recv_info.append(frame)
        if frame == "EOF":
            break
        else:
            soc.send(bytes(f"WORD_${len(recv_info)}","utf-8"))
    soc.close()
    if len(recv_info) > 0:
        content = " ".join(recv_info)
        with open(f"./client_folder/{name_of_file}","w") as f:
            f.write(content)
        print("Data Received :",content)

if __name__ == '__main__':
    
    client()