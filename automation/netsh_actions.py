import subprocess
import platform

class NetshActions:
    @staticmethod
    def run_netsh_command(args):
        if platform.system() != "Windows":
            raise EnvironmentError("Netsh commands only supported on Windows")
        cmd = ["netsh"] + args
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()

    @staticmethod
    def flush_dns():
        return NetshActions.run_netsh_command(["interface", "ip", "set", "dns", "name=\"Ethernet\"", "static", "8.8.8.8"])

    @staticmethod
    def show_dns():
        return NetshActions.run_netsh_command(["interface", "ip", "show", "dns"])

    @staticmethod
    def reset_dns():
        return NetshActions.run_netsh_command(["interface", "ip", "set", "dns", "name=\"Ethernet\"", "dhcp"])

