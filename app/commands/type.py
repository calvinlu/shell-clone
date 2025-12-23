"""
A command that checks whether a command is a builtin, an executable file, or unrecognized.
"""
from app.utils import find_executable

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
    else:
        executable_path = find_executable(argument)
        if executable_path:
            print(f"{argument} is {executable_path}")
        else:
            print(f"{argument} not found")


def is_builtin(argument: str) -> bool:
    """Checks if argument is a builtin"""
    return argument in VALID_BUILTINS
