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