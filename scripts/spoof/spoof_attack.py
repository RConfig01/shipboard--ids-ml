"""
Script: Spoofed Navigation Message Injection
Description: Generates navigation messages with manipulated position data to simulate spoofing attacks.
This script maintains normal-like timing while altering latitude and longitude values.
"""
# Developed as part of an undergraduate dissertation on maritime intrusion detection

# Imports
import socket
import time
import random
from datetime import datetime

# Target IP and port
BRIDGE_IP = "192.168.56.15"
PORT = 5005

# Runtime control
DURATION_SECONDS = 120   # 2 minutes

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Initial vessel position
lat = 51.520
lon = -0.129

# Sequence number
seq = 0

# End time
end_time = time.time() + DURATION_SECONDS

while time.time() < end_time:
    # Larger position changes to simulate spoofed movement
    lat += random.uniform(-0.0045, 0.0045)
    lon += random.uniform(-0.0045, 0.0045)

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
    message += "X" * random.randint(0, 30)

    # Send UDP packet
    sock.sendto(message.encode(), (BRIDGE_IP, PORT))

    # Keep timing fairly close to normal traffic
    time.sleep(random.uniform(1.2, 2.0))

print("Spoof attack generation complete.")
sock.close()
