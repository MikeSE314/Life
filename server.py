import json
import random
import select
import socket
import sys

HOST = 'localhost'
PORT = 8001  # 127.0.0.1
RECV_BUFFER = 4096  # Size of packet

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_list = []  # List of everyone connected

# Staring up the server
try:
    server_socket.bind((HOST, PORT))
except socket.error as error:
    # Server is already running on port 8001
    print('Bind failed. Error Code : %s\nMessage : %s' % (error[0], error[1]))
    sys.exit()

# Add the server to the list of connections
server_socket.listen(30)
connection_list.append(server_socket)
connection_dict = {"server": server_socket}

print("Chat server started on port %s" % PORT)
key = "0123456789abcdef"
iv = " ".join(str(random.randint(0, 255)) for i in range(16))

while True: # kelly.lent@gmail.com
    read_sockets, write_sockets, error_sockets = select.select(connection_list,[],[])
    for s in read_sockets:
        if s == server_socket:
            # A client connected to the server
            conn, addr = server_socket.accept()
            print('Connected with %s:%s' % (addr[0], addr[1]))
            connection_list.append(conn)
            encryption_info = {
                "key": key,
                "iv": iv,
            }
            conn.sendall(json.dumps(encryption_info))
        else:
            # Encryption. Change this to your logic
            try:
                data = s.recv(RECV_BUFFER)
            except socket.error as error:
                print("error", error)
                s.close()
                connection_list.remove(s)
            else:
                if data.startswith("NAME"):
                    name = data.split("|")[1]
                    connection_dict[name] = s
                elif data.startswith("MESSAGE|"):
                    splits = data.split("|")
                    name = splits[1]
                    message = splits[2]
                    connection_dict[name].sendall(message)
server_socket.close()
