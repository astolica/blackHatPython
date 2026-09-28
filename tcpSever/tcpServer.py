import socket 
import threading # allows you to run multiple operations on a single process 

IP = '0.0.0.0' # pass port and IP you want to listen on your device 
PORT = 9998

def main(): 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5) # start listening with max connections of 5 
    print(f'[*] Listening on {IP} Port: {PORT}')

    while True: 
        client, address = server.accept() # activated when we connect 
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket): 
    with client_socket as sock: 
        request = sock.recv(1024)
        print(f"[*] Received: {request.decode("utf-8")}")
        sock.send(b'ACK')


if __name__ == '__main__':
    main() 
    
