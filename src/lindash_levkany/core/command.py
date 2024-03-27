from enum import IntEnum
import subprocess


class CommandType(IntEnum):
    READ = 1
    WRITE = 2


class Command():
    def __init__(self, type:CommandType=CommandType.READ, func:object=None):
        self.__type = type
        self.__func = func
                
        
    @property
    def func(self):
        return self.__func
    
        
    @property
    def type(self):
        return self.__type
    
    
    @type.setter
    def type(self, type:CommandType=CommandType.READ):
        self.__type == type
    
        
    def execute(self, func:object=None) -> int:
        if func:
            return func()

        return self.__func()
