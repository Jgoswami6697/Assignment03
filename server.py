import socket
import json
from datetime import datetime
from collections import defaultdict
import time

# Load configuration from a JSON file
with open('config.json', 'r') as f:
    config = json.load(f)
