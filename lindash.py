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
    
    NOTE:
    this entry point script is temporary, the 
    project will use cli only
    
    example usage:
    
    setting lindash server
    lindash start 0.0.0.0:8888
    
    
    retrieve data via lindash
    lindash 0.0.0.0:8888
"""

from core.server import Lindash
import argparse
import socket
from typing import Tuple
from commands import system
from core.command_chain import CommandChain


def connect_to_lindash(args):
    """connect to a remote lindash server"""
    
    address='0.0.0.0'
    port=8888

    if args.host.count(":"):
        address, port = args.host.split(':')
    
    lindash = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lindash.connect((address, int(port)))
    
    res = lindash.recv(1024)
    print(res.decode())


def on_connected(connection:socket.socket, addr:Tuple[str, int]):
    """callback function when a new connection to lindash established"""

    chain = CommandChain([
        system.list_dir_hidden
    ])
    output = chain.execute()
    connection.send(output.encode())


def start_lindash(args):
    """starts lindash server"""
    
    address='0.0.0.0'
    port=8888
    max_queue=1

    if args.host.count(":"):
        address, port = args.host.split(':')
        
    with Lindash(address, int(port), max_queue, on_connected=on_connected) as server:
        server.start()


parser = argparse.ArgumentParser(
    prog='Lindash - v0.1',
    description='retrieve information about the linux system',
    epilog='see GNU license for more details'
)
sp = parser.add_subparsers()
sp_start = sp.add_parser('start', help='Starts %(prog)s server')
sp_start.add_argument('host')
sp_start.set_defaults(func=start_lindash)

sp_get = sp.add_parser('get', help='connects to server')
sp_get.add_argument('host')
sp_get.set_defaults(func=connect_to_lindash)

args = parser.parse_args()
args.func(args)
