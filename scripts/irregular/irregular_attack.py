"""
Script: Irregular Communication Timing
Description: Generates navigation traffic with inconsistent transmission intervals to simulate timing-based anomalies.
This script varies packet inter-arrival times to disrupt normal communication patterns.
"""
# Developed as part of an undergraduate dissertation on maritime intrusion detection

# Import
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
lat = 51.517
lon = -0.131

# Sequence number
seq = 0

# End time
end_time = time.time() + DURATION_SECONDS

while time.time() < end_time:
    # Natural vessel drift
    lat += random.uniform(-0.002, 0.002)
    lon += random.uniform(-0.002, 0.002)

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

    # Irregular timing behaviour
    r = random.random()

    if r < 0.25:
        sleep_time = random.uniform(0.2, 0.7)   # unusually fast
    elif r < 0.50:
        sleep_time = random.uniform(2.5, 3.8)   # delayed
    else:
        sleep_time = random.uniform(1.2, 2.0)   # normal-like

    time.sleep(sleep_time)

print("Irregular timing attack generation complete.")
sock.close()
