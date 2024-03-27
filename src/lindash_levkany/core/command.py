from enum import IntEnum
import subprocess


class CommandType(IntEnum):
    READ = 1
    WRITE = 2


class Command():
    def __init__(self, type:CommandType=CommandType.READ, cmd:str=None):
        self.__type = type
        self.__cmd = cmd
        
        
    @property
    def cmd(self):
        return self.__cmd
    
        
    @property
    def type(self):
        return self.__type
    
    
    @type.setter
    def type(self, type:CommandType=CommandType.READ):
        self.__type == type
    
        
    def execute(self, cmd:str=None) -> int:
        return subprocess.check_output(cmd or self.__cmd, shell=True)
        