from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSlider
from PyQt6.QtCore import Qt

class CustomControls(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        
        self.refresh_button = QPushButton("Refresh")
        self.kill_button = QPushButton("Kill Process")
        
        self.refresh_slider = QSlider(Qt.Orientation.Horizontal)
        self.refresh_slider.setRange(500, 5000)
        self.refresh_slider.setValue(1000)

        self.layout.addWidget(self.refresh_button)
        self.layout.addWidget(self.kill_button)
        self.layout.addWidget(self.refresh_slider)
        self.setLayout(self.layout)