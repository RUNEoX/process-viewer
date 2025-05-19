import importlib
import os

class PluginLoader:
    def __init__(self, plugin_dir="plugins"):
        self.plugin_dir = plugin_dir
        self.plugins = []

    def load_plugins(self):
        """Dynamically loads plugins from the plugin directory."""
        for file in os.listdir(self.plugin_dir):
            if file.endswith(".py") and file != "__init__.py":
                module_name = file[:-3]
                try:
                    module = importlib.import_module(f"plugins.{module_name}")
                    self.plugins.append(module)
                    print(f"Loaded plugin: {module_name}")
                except Exception as e:
                    print(f"Error loading plugin {module_name}: {e}")

    def get_plugins(self):
        """Returns the list of loaded plugins."""
        return self.plugins

