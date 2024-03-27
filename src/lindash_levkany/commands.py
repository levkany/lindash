from core.command import Command
from core.command import CommandType
import subprocess


list_dir = Command(
    CommandType.READ,
    lambda: subprocess.check_output("ls -l", shell=True)
)

total_cores = Command(
    CommandType.READ,
    lambda: subprocess.check_output("nproc --all", shell=True)
)

get_python_install_at = Command(
    CommandType.READ,
    lambda: subprocess.check_output("which python3", shell=True)
)
