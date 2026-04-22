import socket

HOST = 'data.pr4e.org'
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
picture = "".encode()
count = 0
print(f"Data_Length  |   Count")
print("="*25)

while True:
    data  = s.recv(1024)
    count = count + len(data)
    if len(data) == 0:
        break
    picture += data
    print(f"{len(data):<12} | {count:<12}")

s.close()

extract = picture.find(b'\r\n\r\n')
picture = picture[extract + 4 ::]

with open ("image.png", "wb") as f:
    f.write(picture)




