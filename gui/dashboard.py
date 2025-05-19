from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import QTimer
import psutil
import GPUtil
from .system_graphs import SystemGraphs

def get_cpu_temp():
    try:
        temps = psutil.sensors_temperatures()
        if not temps:
            return None
        for entries in temps.values():
            for entry in entries:
                label = entry.label.lower()
                if 'cpu' in label or 'package id 0' in label or 'core 0' in label:
                    return entry.current
        # fallback to first available sensor
        for entries in temps.values():
            if entries:
                return entries[0].current
    except (AttributeError, Exception):
        return None

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.title_label = QLabel("System Monitor Dashboard")
        self.cpu_label = QLabel("CPU Usage: N/A")
        self.cpu_temp_label = QLabel("CPU Temp: N/A")
        self.gpu_label = QLabel("GPU Usage: N/A")
        self.gpu_temp_label = QLabel("GPU Temp: N/A")
        self.memory_label = QLabel("Memory Usage: N/A")

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.cpu_label)
        self.layout.addWidget(self.cpu_temp_label)
        self.layout.addWidget(self.gpu_label)
        self.layout.addWidget(self.gpu_temp_label)
        self.layout.addWidget(self.memory_label)

        self.graphs = SystemGraphs()
        self.layout.addWidget(self.graphs)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_metrics)
        self.timer.start(1000)

    def update_metrics(self):
        cpu_percent = psutil.cpu_percent()
        self.cpu_label.setText(f"CPU Usage: {cpu_percent:.1f}%")

        cpu_temp = get_cpu_temp()
        self.cpu_temp_label.setText(f"CPU Temp: {cpu_temp:.1f}°C" if cpu_temp else "CPU Temp: N/A")

        try:
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]
                self.gpu_label.setText(f"GPU Usage: {gpu.load * 100:.1f}%")
                self.gpu_temp_label.setText(f"GPU Temp: {gpu.temperature:.1f}°C")
            else:
                self.gpu_label.setText("GPU Usage: N/A")
                self.gpu_temp_label.setText("GPU Temp: N/A")
        except Exception:
            self.gpu_label.setText("GPU Usage: Error")
            self.gpu_temp_label.setText("GPU Temp: Error")

        mem = psutil.virtual_memory()
        mem_percent = mem.percent
        self.memory_label.setText(f"Memory Usage: {mem_percent:.1f}%")
