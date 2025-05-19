import sys
import logging
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
import sys
import os

def setup_logging():
    logging.basicConfig(
        filename='logs/event.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def main():
    setup_logging()
    logging.info("Starting NetworkRuler application")

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

