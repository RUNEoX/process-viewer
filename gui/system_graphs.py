import psutil
import GPUtil
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import QTimer
import pyqtgraph as pg
import datetime


class SystemGraphs(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)

        self.cpu_plot = self._create_graph("CPU Usage %")
        self.gpu_plot = self._create_graph("GPU Usage %")
        self.disk_plot = self._create_graph("Disk I/O KB/s")

        self.cpu_data = []
        self.gpu_data = []
        self.disk_data = []

        self.time_data = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

    def _create_graph(self, title):
        label = QLabel(title)
        label.setStyleSheet("font-weight: bold; padding-top: 8px;")
        self.layout.addWidget(label)

        plot_widget = pg.PlotWidget()
        plot_widget.setBackground('default')
        plot_widget.showGrid(x=True, y=True)
        plot_widget.setYRange(0, 100)
        plot_widget.addLegend()

        plot = plot_widget.plot(pen='c', name=title)
        self.layout.addWidget(plot_widget)
        return plot

    def update_data(self):
        current_time = datetime.datetime.now().strftime('%H:%M:%S')

        # CPU
        cpu = psutil.cpu_percent()
        self.cpu_data.append(cpu)

        # GPU
        gpus = GPUtil.getGPUs()
        gpu = gpus[0].load * 100 if gpus else 0
        self.gpu_data.append(gpu)

        # Disk
        io = psutil.disk_io_counters()
        read = io.read_bytes
        write = io.write_bytes
        total_kb = (read + write) / 1024
        self.disk_data.append(total_kb)

        self.time_data.append(current_time)

        if len(self.cpu_data) > 30:
            self.cpu_data.pop(0)
            self.gpu_data.pop(0)
            self.disk_data.pop(0)
            self.time_data.pop(0)

        self.cpu_plot.setData(self.cpu_data, pen='g')
        self.gpu_plot.setData(self.gpu_data, pen='m')
        self.disk_plot.setData(self.disk_data, pen='y')
