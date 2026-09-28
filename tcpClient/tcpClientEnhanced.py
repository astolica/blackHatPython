""" 
TCP Client with a little more 'oomph'
"""

import socket 

target_host = input("Provide a target host: \n")
target_port =  input("Provide a target port: \n")

# create a socket object
# AF_INET indicates that we willuse a standard IPv4 address or host name 
# SOCK_STREAM indicates that this will be a TCP client 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting the client
client.settimeout(5)
try:  
    client.connect((target_host, target_port))
except socket.gaierror: 
    print("Hostname cannot be resolved, check DNS or typos in the hostname.")
except ConnectionRefusedError:
    print("Host cannot be reached, port not active.")
except socket.timeout:
    print("Cannot connect to host as it may not be active. Perhaps a firewall filter is in place?")

# request message 
request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n"

# encode request as bytes 
client.sendall(request.encode())

# receive data
response = client.recv(4096)
while response != b"": 
    print(response.decode(errors="replace")) # bytes that can't be read are replaced with a unicode character

with socket.socket() as client: 
    client.close() 
