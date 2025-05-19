from PyQt6.QtWidgets import QMainWindow, QComboBox, QVBoxLayout, QWidget, QTabWidget
from gui.theme_manager import ThemeManager
from gui.dashboard import Dashboard
from gui.process_tree import ProcessTree

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Process Viewer")
        self.resize(900, 700)

        self.themes = ['dark', 'light', 'pink', 'purple']
        self.theme_manager = ThemeManager(self)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.theme_selector = QComboBox()
        self.theme_selector.addItems([t.capitalize() + " Mode" for t in self.themes])
        self.theme_selector.currentTextChanged.connect(self.change_theme)
        self.layout.addWidget(self.theme_selector)

        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        self.dashboard_tab = Dashboard()
        self.tabs.addTab(self.dashboard_tab, "Dashboard")

        self.process_tree_tab = ProcessTree()
        self.tabs.addTab(self.process_tree_tab, "Process Tree")

        self.theme_manager.apply_theme(self.themes[0])

    def change_theme(self, selected_text):
        selected_theme = selected_text.lower().split()[0] 
        self.theme_manager.apply_theme(selected_theme)
