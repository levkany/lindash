"""
    Copyright (c) 2024 levkany
    All rights reserved.

    The source code, including any accompanying documentation
    or files, is the exclusive property of levkany
    ("Owner") and is confidential and proprietary.

    No part of the source code may be reproduced, distributed,
    or transmitted in any form or by any means, including photocopying,
    recording, or other electronic or mechanical methods,
    without the prior written permission of the Owner.

    Unauthorized use, reproduction, or distribution of the source code
    or any portion thereof is strictly prohibited and may result
    in severe civil and criminal penalties.

    For licensing inquiries, please contact levkany.dev@gmail.com
"""


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