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


import socket as s
from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from socket import SOL_SOCKET
from socket import SO_REUSEADDR
import logging
import traceback


class Lindash():
    def __init__(self, address='0.0.0.0', port=8888, max_queue=1, on_connected=None):
        """`Lindash`

        Args:
            `address` (str, optional): the address the listen will listen for connection on. Defaults to '0.0.0.0'.
            `port` (int, optional): the port the server will listen for connection on. Defaults to 8888.
            `max_queue` (int, optional): maximum pending connections for the server. Defaults to 1.
        """
        self.listen_address = address
        self.listen_port = port
        self.max_queue = max_queue
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.connections = []
        self.on_connected_callback = on_connected
        self.stopped = False
        
        self.logger = logging.getLogger(__name__)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s', datefmt='%d/%m/%y %H:%M')
        logging_handler = logging.StreamHandler()
        logging_handler.setLevel(logging.INFO)
        logging_handler.setFormatter(formatter)
        self.logger.addHandler(logging_handler)
        self.logger.setLevel(logging.INFO)
        
        
    def __enter__(self): 
        return self
    
    
    def __exit__(self, exc_type, exc_value, traceback):
        if not self.stopped:
            self.stop()
        
        
    def stop(self):
        self.logger.info('stopping server ..')
        self.socket.shutdown(s.SHUT_RDWR)
        self.socket.close()
        self.stopped = True
        
    
    def start(self):
        """start the server and wait for connections
        """
        
        self.socket.bind((self.listen_address, self.listen_port))
        self.socket.listen(self.max_queue)
        self.logger.info('server is ready to accept connections')

        while True:
            try:
                
                client, addr = self.socket.accept()
                self.logger.info(f"new connection established: {addr}")
                self.on_connected_callback(client, addr)
                client.shutdown(s.SHUT_RDWR)
                client.close()
                                
            except: 
                self.logger.info(traceback.format_exc())
                break
            

        #
        #   start has stopped, clean up, etc
        #
        
        if not self.stopped:
            self.stop()
