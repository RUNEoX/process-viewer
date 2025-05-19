import subprocess
import threading
import logging
import json

logger = logging.getLogger(__name__)

class ScriptTrigger:
    def __init__(self):
        self.watchers = []

    def add_watch(self, condition_func, script_path):
        """Register a script to run when condition_func returns True."""
        self.watchers.append((condition_func, script_path))

    def start(self, poll_interval=1):
        def watcher_loop():
            while True:
                for condition_func, script_path in self.watchers:
                    try:
                        if condition_func():
                            logger.info(f"Triggering script: {script_path}")
                            subprocess.Popen(script_path, shell=True)
                    except Exception as e:
                        logger.error(f"Error in script trigger: {e}")
                threading.Event().wait(poll_interval)
        thread = threading.Thread(target=watcher_loop, daemon=True)
        thread.start()

