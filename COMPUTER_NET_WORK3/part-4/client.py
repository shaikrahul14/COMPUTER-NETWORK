import socket
from PIL import Image
host = '127.0.0.1'
port = 4567

temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
temp.connect((host, port))
print("Connecting to the server...\n")


with open('ClientFolder/a.jpg', 'wb') as f:
        print('To save the received image, a new file has been generated.')
        data = temp.recv(100000)
        f.write(data)
        print("collect recived data from the server ")  
        f.close()





with open('ClientFolder/a.jpg', 'rb') as f:
        rahul = Image.open(f)
        rahul.show()




print(' RECEIVED image')
temp.close()
print('successfully executed the program')