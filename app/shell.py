"""
A simple shell implementation that provides a basic command-line interface.

This module implements a minimal shell that can be extended with additional commands.
Currently supports the 'exit' command to terminate the shell.
"""
import os
import subprocess
import sys
from app.commands.echo import command_echo
from app.commands.type import command_type
from app.utils import find_executable

def shell():
    """ Shell function containing the main loop """
    while True:
        sys.stdout.write("$ ")
        user_input = input().strip()

        user_input = user_input.split()

        command = user_input[0]
        args = user_input[1:]

        if find_executable(command):
            subprocess.Popen([command] + args)
            continue
        
        match command:
            case "exit":
                break
            case "echo":
                command_echo(args)
            case "type":
                command_type(args)
            case _:
                print(f"{command}: command not found")
                continue
