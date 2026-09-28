"""
From the book, just as a base example. See READEME.md for credits
"""

import socket 

target_host = input("Provide a target host: \n")
target_port = 9998 

# create a socket object
# AF_INET indicates that we willuse a standard IPv4 address or host name 
# SOCK_STREAM indicates that this will be a TCP client 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting the client 
client.connect((target_host, target_port))

# sending data 

request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n"

# encode request as bytes 
client.send(request.encode())

# receive data
response = client.recv(4096)

print(response.decode())
client.close()
