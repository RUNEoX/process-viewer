import os
import importlib
import logging

logger = logging.getLogger(__name__)

class PluginManager:
    def __init__(self, plugins_folder='plugins'):
        self.plugins_folder = plugins_folder
        self.plugins = []

    def discover_plugins(self):
        if not os.path.isdir(self.plugins_folder):
            logger.warning(f"Plugins folder not found: {self.plugins_folder}")
            return

        for filename in os.listdir(self.plugins_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                try:
                    module = importlib.import_module(f'{self.plugins_folder}.{module_name}')
                    if hasattr(module, 'register_plugin'):
                        module.register_plugin()
                    self.plugins.append(module)
                    logger.info(f"Loaded plugin: {module_name}")
                except Exception as e:
                    logger.error(f"Failed to load plugin {module_name}: {e}")

    def get_plugins(self):
        return self.plugins

