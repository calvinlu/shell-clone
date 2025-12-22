"""
A simple shell implementation that provides a basic command-line interface.

This module implements a minimal shell that can be extended with additional commands.
Currently supports the 'exit' command to terminate the shell.
"""
import sys

def shell():
    """ Shell function containing the main loop """
    while True:
        sys.stdout.write("$ ")
        command = input().strip()
        match command:
            case "exit":
                break
            case _:
                print(f"{command}: command not found")
                continue
