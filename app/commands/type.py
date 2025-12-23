"""
A command that checks whether a command is a builtin, an executable file, or unrecognized.
"""
import os

TYPE_COMMAND = "type"

VALID_BUILTINS = ["echo", "type", "exit"]

def command_type(args: list[str]):
    """ Type the arguments """
    if len(args) == 0:
        print("type: missing operand")
        return
    argument = args[0]

    if is_builtin(argument):
        print(f"{argument} is a shell builtin")
    elif is_executable(argument):
        print(f"{argument} is {os.path.abspath(argument)}")
    else:
        print(f"{argument} not found")

def is_builtin(argument: str) -> bool:
    """Checks if argument is a builtin"""
    return argument in VALID_BUILTINS

def is_executable(argument: str) -> bool:
    """Checks if argument is an executable file"""
    return os.path.exists(argument) and os.access(argument, os.X_OK)
