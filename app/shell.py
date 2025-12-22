"""
A simple shell implementation that provides a basic command-line interface.

This module implements a minimal shell that can be extended with additional commands.
Currently supports the 'exit' command to terminate the shell.
"""
import sys
from app.commands.echo import echo

def shell():
    """ Shell function containing the main loop """
    while True:
        sys.stdout.write("$ ")
        user_input = input().strip()

        user_input = user_input.split()

        command = user_input[0]
        args = user_input[1:]

        match command:
            case "exit":
                break
            case "echo":
                echo(args)
            case _:
                print(f"{user_input}: command not found")
                continue
