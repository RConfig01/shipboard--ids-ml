"""
Script: Normal Traffic Generator
Description: Generates baseline AIS/GNSS-style traffic for the simulated shipboard network.
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
DURATION_SECONDS = 180

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
    # Natural vessel drift
    lat += random.uniform(-0.0015, 0.0015)
    lon += random.uniform(-0.0015, 0.0015)

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

    # Mostly regular timing with slight natural variation
    if random.random() < 0.1:
        sleep_time = random.uniform(0.7, 1.2)
    else:
        sleep_time = random.uniform(1.4, 2.3)

    time.sleep(sleep_time)

print("Normal traffic generation complete.")
sock.close()
