import psutil
import time

with open("cpu_log.txt", "a") as f:
    while True:
        usage = psutil.cpu_percent()
        f.write(f"{time.time()} {usage}\n")
        time.sleep(1)
