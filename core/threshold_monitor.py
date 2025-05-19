import psutil
from datetime import datetime

class ThresholdMonitor:
    def __init__(self, cpu_threshold=80, mem_threshold=80):
        self.cpu_threshold = cpu_threshold
        self.mem_threshold = mem_threshold
        self.log = []

    def check_thresholds(self):
        """Checks if any process exceeds set thresholds."""
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                if proc.info['cpu_percent'] > self.cpu_threshold or proc.info['memory_percent'] > self.mem_threshold:
                    self.log_event(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    def log_event(self, proc_info):
        """Logs threshold breach events."""
        event = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "pid": proc_info['pid'],
            "name": proc_info['name'],
            "cpu": proc_info['cpu_percent'],
            "memory": proc_info['memory_percent'],
        }
        self.log.append(event)
        print(f"Threshold exceeded: {event}")

    def get_log(self):
        """Returns the list of threshold breach events."""
        return self.log

