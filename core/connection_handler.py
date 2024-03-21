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


from threading import Thread
from socket import socket
import time


class ConnectionHandler():
    def __init__(self, connection:socket):
        self.connection = connection
        self.stopped = False
    
        
    def stop(self):
        print('closing connected client')
        # TODO: figure out a way to stop the thread since it is running indefinitely
        if self.thread.is_alive():
            del self.thread
            
        self.stopped = True
        
        
    def start(self):
        self.thread = Thread(target=self.runner, args=(self.connection,))
        self.thread.start()
        self.stopped = False
        
        with Runner() as runner:
            
        
        
    def runner(self, connection:socket):
        try:
            while True:
                data = connection.recv(1024)
                if data:
                    print(f"got data o length: {data.__len__()}")
        except: ...
