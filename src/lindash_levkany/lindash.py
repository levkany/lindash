import argparse
from commands import system
from core.command_chain import CommandChain


def handle_exec(c:str):
    """callback for command execution"""

    chain = CommandChain([
        system.total_cores
    ])
    output = chain.execute()
    print(output)


parser = argparse.ArgumentParser(
    prog='Lindash - 0.0.1',
    description='linux cli tool for servers',
    epilog='see GNU license for more details'
)
parser.add_argument('-c', required=True)
parser.set_defaults(func=handle_exec)
args = parser.parse_args()
args.func(args)
