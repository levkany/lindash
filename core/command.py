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


from enum import IntEnum
import os
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
        