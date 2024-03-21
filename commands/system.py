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


from core.command import Command
from core.command import CommandType


list_dir = Command(
    CommandType.READ,
    'ls -l'
)

list_dir_hidden = Command(
    CommandType.READ,
    'ls -la'
)

clear = Command(
    CommandType.READ,
    'clear'
)
