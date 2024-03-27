from .command import Command
from typing import List


class CommandChain():
    def __init__(self, commands:List[Command]=[]) -> None:
        self.__commands = commands
        self.__output = ''
    
    
    @property
    def output(self) -> str:
        return self.__output
    
        
    @property
    def commands(self) -> List[Command]:
        return self.__commands
    
    
    @commands.setter
    def commands(self, commands:List[Command]) -> None:
        self.__commands = commands
        
        
    def add(self, command:Command) -> None:
        self.__commands.append(command)
    
    
    def execute(self):
        for command in self.__commands:
            output = command.execute()
            self.__output += f"{output.decode()}\r\n"
        
        output = self.__output
        self.__output = ''
        return output