from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from core import stealth_mode

class StealthToggle(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QHBoxLayout())

        self.label = QLabel("Stealth Mode: OFF")
        self.toggle_button = QPushButton("Activate Stealth")

        self.layout().addWidget(self.label)
        self.layout().addWidget(self.toggle_button)

        self.toggle_button.clicked.connect(self.toggle_stealth)

    def toggle_stealth(self):
        if stealth_mode.is_stealth_active():
            stealth_mode.deactivate_stealth()
            self.label.setText("Stealth Mode: OFF")
            self.toggle_button.setText("Activate Stealth")
        else:
            stealth_mode.activate_stealth()
            self.label.setText("Stealth Mode: ON")
            self.toggle_button.setText("Deactivate Stealth")
