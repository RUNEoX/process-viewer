import psutil
import json

class ProcessManager:
    def __init__(self):
        self.processes = []

    def fetch_processes(self):
        """Fetches current system processes."""
        self.processes = []
        for proc in psutil.process_iter(attrs=['pid', 'name', 'username', 'cpu_percent', 
                                               'memory_percent', 'io_counters', 'num_threads']):
            try:
                self.processes.append(proc.info)
            except psutil.NoSuchProcess:
                continue
        return self.processes

    def adjust_priority(self, pid, priority):
        """Sets the priority of a process."""
        try:
            proc = psutil.Process(pid)
            proc.nice(priority)
            return f"Priority set to {priority} for PID {pid}"
        except (psutil.NoSuchProcess, PermissionError) as e:
            return str(e)

    def set_cpu_affinity(self, pid, cpus):
        """Sets the CPU affinity for a process."""
        try:
            proc = psutil.Process(pid)
            proc.cpu_affinity(cpus)
            return f"CPU affinity set to {cpus} for PID {pid}"
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            return str(e)

    def send_signal(self, pid, signal):
        """Sends a signal to the process."""
        try:
            proc = psutil.Process(pid)
            proc.send_signal(signal)
            return f"Signal {signal} sent to PID {pid}"
        except (psutil.NoSuchProcess, PermissionError) as e:
            return str(e)

    def export_to_json(self, filename="processes.json"):
        """Exports the current process list to a JSON file."""
        with open(filename, "w") as f:
            json.dump(self.processes, f, indent=4)
        return f"Processes exported to {filename}"

    def set_cpu_affinity(pid: int, cores: list[int]):
        p = psutil.Process(pid)
        p.cpu_affinity(cores)

    def suspend_process(pid: int):
        psutil.Process(pid).suspend()

    def resume_process(pid: int):
        psutil.Process(pid).resume()
