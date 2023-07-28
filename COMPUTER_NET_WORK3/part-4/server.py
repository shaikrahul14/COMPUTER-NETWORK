import socket
from PIL import Image
portnumber = 4567
host = '127.0.0.1'
temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

temp.bind((host, portnumber))
temp.listen(1)

print('Server has ready. search for any clients trying to connect.')
while True:
    connection, addr_ess = temp.accept()
    if connection:


        print(f'Connecting to {addr_ess}...')


        with open('ServerFolder/b.jpg', 'rb') as f:
            connection.sendall(f.read())
            f.close()
            break
        
print('successfully executed the program')