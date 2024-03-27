from core.command import Command
from core.command import CommandType


list_dir = Command(
    CommandType.READ,
    'ls -l'
)

list_dir_hidden = Command(
    CommandType.READ,
    'ls -la'
)

clear = Command(
    CommandType.READ,
    'clear'
)

total_cores = Command(
    CommandType.READ,
    'nproc --all'
)