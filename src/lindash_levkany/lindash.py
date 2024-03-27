import argparse
from commands import system
from core.command_chain import CommandChain


def handle_exec(c:str):
    """callback function when a new connection to lindash established"""

    chain = CommandChain([
        system.total_cores
    ])
    output = chain.execute()
    print(output)


parser = argparse.ArgumentParser(
    prog='Lindash - v0.1',
    description='retrieve information about the linux system',
    epilog='see GNU license for more details'
)

parser.add_argument('-c', required=True)
parser.set_defaults(func=handle_exec)

args = parser.parse_args()
args.func(args)
