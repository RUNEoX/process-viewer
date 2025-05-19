import os
from PyQt6.QtWidgets import QApplication

class ThemeManager:
    def __init__(self, app: QApplication, style_path='assets/styles'):
        self.app = app
        self.style_path = style_path
        self.current_theme = 'dark'
        self.available_themes = {
            'dark': 'dark.qss',
            'light': 'light.qss',
            'pink': 'pink.qss',
            'purple': 'purple.qss'
        }

    def apply_theme(self, theme_name):
        if theme_name not in self.available_themes:
            return

        theme_file = os.path.join(self.style_path, self.available_themes[theme_name])
        if os.path.exists(theme_file):
            with open(theme_file, 'r') as f:
                self.app.setStyleSheet(f.read())
            self.current_theme = theme_name
