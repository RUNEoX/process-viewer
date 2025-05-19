from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QTreeWidget, QTreeWidgetItem,
    QPushButton, QCheckBox, QMessageBox, QComboBox, QLabel
)
import psutil
import signal
import sys

class ProcessTree(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

        controls_layout = QHBoxLayout()
        self.main_apps_cb = QCheckBox("Show Main Apps")
        self.main_apps_cb.setChecked(True)
        self.main_apps_cb.stateChanged.connect(self.toggle_main_apps)

        self.bg_services_cb = QCheckBox("Show Background/Services")
        self.bg_services_cb.setChecked(True)
        self.bg_services_cb.stateChanged.connect(self.toggle_bg_services)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh_processes)

        self.kill_button = QPushButton("Kill Process")
        self.kill_button.clicked.connect(self.kill_selected_process)

        # Priority controls
        self.priority_label = QLabel("Set Priority:")
        self.priority_combo = QComboBox()
        self.priority_combo.addItems(["Idle", "Below Normal", "Normal", "Above Normal", "High", "Realtime"])
        self.set_priority_button = QPushButton("Set Priority")
        self.set_priority_button.clicked.connect(self.set_priority_for_selected)

        controls_layout.addWidget(self.main_apps_cb)
        controls_layout.addWidget(self.bg_services_cb)
        controls_layout.addWidget(self.refresh_button)
        controls_layout.addWidget(self.kill_button)
        controls_layout.addWidget(self.priority_label)
        controls_layout.addWidget(self.priority_combo)
        controls_layout.addWidget(self.set_priority_button)
        self.layout().addLayout(controls_layout)

        self.tree_layout = QHBoxLayout()
        self.layout().addLayout(self.tree_layout)

        self.main_apps_tree = QTreeWidget()
        self.main_apps_tree.setHeaderLabels(["Main Apps - Process Name", "PID", "CPU %", "Memory MB"])
        self.tree_layout.addWidget(self.main_apps_tree)

        self.bg_services_tree = QTreeWidget()
        self.bg_services_tree.setHeaderLabels(["Background/Services - Process Name", "PID", "CPU %", "Memory MB"])
        self.tree_layout.addWidget(self.bg_services_tree)

        self.refresh_processes()

    def toggle_main_apps(self):
        self.main_apps_tree.setVisible(self.main_apps_cb.isChecked())

    def toggle_bg_services(self):
        self.bg_services_tree.setVisible(self.bg_services_cb.isChecked())

    def refresh_processes(self):
        self.main_apps_tree.clear()
        self.bg_services_tree.clear()

        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'username', 'status']):
            try:
                info = proc.info
                name = info['name'] or "Unknown"
                pid = info['pid']
                cpu = info['cpu_percent'] or 0.0
                mem = info['memory_info'].rss / (1024 * 1024)
                item = QTreeWidgetItem([name, str(pid), f"{cpu:.1f}", f"{mem:.1f}"])
                if self.is_main_app(proc):
                    self.main_apps_tree.addTopLevelItem(item)
                else:
                    self.bg_services_tree.addTopLevelItem(item)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    def is_main_app(self, proc):
        try:
            if proc.username() and proc.status() != psutil.STATUS_SLEEPING:
                if proc.username().lower() not in ['system', 'localservice', 'networkservice']:
                    return True
            return False
        except psutil.Error:
            return False

    def kill_selected_process(self):
        selected = self.main_apps_tree.currentItem()
        if not selected:
            selected = self.bg_services_tree.currentItem()

        if not selected:
            QMessageBox.warning(self, "No Selection", "Please select a process to kill.")
            return

        pid = int(selected.text(1))
        confirm = QMessageBox.question(
            self,
            "Confirm Kill",
            f"Are you sure you want to kill process PID {pid}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            try:
                p = psutil.Process(pid)
                p.terminate()
                p.wait(timeout=3)
                self.refresh_processes()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired) as e:
                QMessageBox.critical(self, "Error", f"Failed to kill process: {e}")

    def set_priority_for_selected(self):
        selected = self.main_apps_tree.currentItem()
        if not selected:
            selected = self.bg_services_tree.currentItem()

        if not selected:
            QMessageBox.warning(self, "No Selection", "Please select a process to set priority.")
            return

        pid = int(selected.text(1))
        priority_str = self.priority_combo.currentText()

        priority_map = {
            "Idle": psutil.IDLE_PRIORITY_CLASS,
            "Below Normal": psutil.BELOW_NORMAL_PRIORITY_CLASS,
            "Normal": psutil.NORMAL_PRIORITY_CLASS,
            "Above Normal": psutil.ABOVE_NORMAL_PRIORITY_CLASS,
            "High": psutil.HIGH_PRIORITY_CLASS,
            "Realtime": psutil.REALTIME_PRIORITY_CLASS,
        }

        try:
            p = psutil.Process(pid)
            if sys.platform == "win32":
                p.nice(priority_map.get(priority_str, psutil.NORMAL_PRIORITY_CLASS))
            else:
                unix_priority_map = {
                    "Idle": 19,
                    "Below Normal": 10,
                    "Normal": 0,
                    "Above Normal": -5,
                    "High": -10,
                    "Realtime": -20,
                }
                p.nice(unix_priority_map.get(priority_str, 0))
            QMessageBox.information(self, "Success", f"Priority set to {priority_str} for PID {pid}")
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            QMessageBox.critical(self, "Error", f"Failed to set priority: {e}")
