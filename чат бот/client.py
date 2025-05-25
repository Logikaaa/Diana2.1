from socket import*
import threading

client_socket = socket(AF_INET, SOCK_STREAM)
name = input("Введіть ім'я")
client_socket.connect("localhost", 8888)
client_socket.send(name.encode())

def send_messege():
    while True:
        client_messege = input()
        if client_messege.lower() == "exit":
            client_socket.close()
            break
        client_socket.send(client_messege.encode())

while True:
    try:
        messege = client_socket.recv(1024).decode().strip()
        if messege:
            print(messege)
            
    except:
        break
        