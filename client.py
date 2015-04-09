from Crypto.Cipher import AES
import json
import select
import socket
import sys
import time


HOST = 'localhost'  # 127.0.0.1
PORT = 8001
RECV_BUFFER = 4096
mode = AES.MODE_CBC

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))
except Exception as error:
    print("Could not connect to the server: %s" % error)

data = client_socket.recv(RECV_BUFFER)
encryption_information = json.loads(data)
key = encryption_information["key"]
iv = encryption_information["iv"]
iv = "".join([chr(int(x)) for x in iv.split()])

def sender():
    client_socket.send("NAME|SENDER")
    count = 0
    while True:
        time.sleep(1)
        count += 1
        message = "Sending data to RECEIVER %s" % count
        padding_width = 16 - len(message) % 16
        print(len(message), padding_width)
        message = message.ljust(len(message) + padding_width)
        encryptor = AES.new(key, mode, IV=iv)
        data = encryptor.encrypt(message)
        client_socket.send("MESSAGE|RECEIVER|%s" % data)

def receiver():
    client_socket.send("NAME|RECEIVER")
    while True:
        data = client_socket.recv(RECV_BUFFER)
        print(len(data))
        decryptor = AES.new(key, mode, IV=iv)
        try:
            data = decryptor.decrypt(data)
        except ValueError:
            print("Could not decrypt message")
        else:
            print("got message: %s" % data)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sender()
    else:
        receiver()