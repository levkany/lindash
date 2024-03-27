import argparse
from core.command_chain import CommandChain
import config
import logging
import commands


logger = logging.getLogger(__name__)


def handle_exec(args:str) -> str:
    """callback for command execution"""
    
    chain = CommandChain()
    
    for c in args.c:    
        if c not in config.ALLOWED_COMMANDS:
            logger.error(f"(error: 4001) - \"{c}\" Command is not allowed to be executed")
            exit(4001)
            
        func = getattr(commands, c)
        chain.add(func)
    
    output = chain.execute()
    print(output)


parser = argparse.ArgumentParser(
    prog='Lindash - 0.0.1',
    description='linux cli tool for servers',
    epilog='see GNU license for more details'
)
parser.add_argument('-c', required=True, action='append')
parser.set_defaults(func=handle_exec)
args = parser.parse_args()
args.func(args)
