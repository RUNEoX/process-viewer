import psutil

class TreeView:
    def __init__(self):
        self.tree = {}

    def build_tree(self):
        """Constructs a parent-child tree of processes."""
        self.tree = {}
        for proc in psutil.process_iter(['pid', 'ppid', 'name']):
            pid = proc.info['pid']
            ppid = proc.info['ppid']
            if ppid not in self.tree:
                self.tree[ppid] = []
            self.tree[ppid].append((pid, proc.info['name']))
        return self.tree

    def get_tree(self):
        """Returns the current process tree."""
        return self.tree

