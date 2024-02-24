import socket
import json
from datetime import datetime
from collections import defaultdict
import time

# Load configuration from a JSON file
with open('config.json', 'r') as f:
    config = json.load(f)

HOST = config['HOST']  # Standard loopback interface address (localhost)
PORT = config['PORT']  # Port to listen on (non-privileged ports are > 1023)

def log(message, level):
    with open('log.txt', 'a') as f:
        f.write(f'{datetime.now()} - {level} - {message}\n')

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    log('Server is listening', 'INFO')

    while True:
        # Wait for a connection
        try:
            conn, addr = s.accept()
            with conn:
                log(f'Connected by {addr}', 'INFO')
                data = conn.recv(1024)
                if not data:
                    log(f'Client {addr} disconnected', 'INFO')
                    break
                message = data.decode('utf-8')

                # Update the message count and start time for this client
                message_counts[addr] += 1
                if message_counts[addr] == 1:
                    start_times[addr] = time.time()
