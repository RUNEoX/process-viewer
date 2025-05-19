import socket
import requests
import time
import psutil

url = 'https://speed.hetzner.de/100MB.bin'
start = time.time()
r = requests.get(url, stream=True)
bytes_read = 0
for chunk in r.iter_content(chunk_size=8192):
    bytes_read += len(chunk)
    if bytes_read > 1024 * 1024: 
        break
end = time.time()
speed = bytes_read / (end - start) / 1024  
print(f"Download speed: {speed:.2f} KB/s")
def get_bandwidth_usage():
    counters = psutil.net_io_counters(pernic=True)
    return {iface: (counters[iface].bytes_sent, counters[iface].bytes_recv) for iface in counters}
ip = '127.0.0.1'
for port in range(20, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} open")
    sock.close()
