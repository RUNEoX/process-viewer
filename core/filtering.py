import re

class ProcessFilter:
    @staticmethod
    def filter_by_name(processes, name):
        return [p for p in processes if name.lower() in p.get('name', '').lower()]

    @staticmethod
    def filter_by_user(processes, user):
        return [p for p in processes if p.get('username', '') == user]

    @staticmethod
    def filter_by_command(processes, regex):
        pattern = re.compile(regex)
        return [p for p in processes if pattern.search(p.get('cmdline', ''))]

    @staticmethod
    def sort_processes(processes, key, reverse=False):
        return sorted(processes, key=lambda p: p.get(key, ''), reverse=reverse)
