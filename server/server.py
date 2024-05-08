import socket 
from threading import Thread

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost",5555))

server.listen()
all_client={}

def client_thread(client):
    while True:
        try:
            msg = client.recv(1024)
            for c in all_client:
                c.send(msg)

        except:
            for c in all_client:
                if c!=client:
                    c.send(f"{name} has left the chat".encode())

            del all_client[client]
            client.close()
            break

while True:
    print("waiting for connections...")
    client, address = server.accept()
    print("connection established")
    name = client.recv(1024).decode()
    all_client[client] = name 
    
    for c in all_client:
        if c!=client:
            c.send(f"{name} has joined the chat".encode())
    
    thread = Thread(target=client_thread,args=(client,))
    thread.start()