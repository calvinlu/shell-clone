"""
A command that changes the current working directory.
"""

import os

def command_cd(path: str):
    """ Changes the current working directory to the specified path. """
    if path:
        os.chdir(path)
