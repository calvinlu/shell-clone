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
    else:
        executable_path = find_executable(argument)
        if executable_path:
            print(f"{argument} is {executable_path}")
        else:
            print(f"{argument} not found")


def is_builtin(argument: str) -> bool:
    """Checks if argument is a builtin"""
    return argument in VALID_BUILTINS


def find_executable(argument: str) -> str:
    """Find the full path to an executable in PATH"""
    if os.path.isabs(argument):
        if os.path.isfile(argument) and os.access(argument, os.X_OK):
            return argument
        return ""

    for path in os.environ.get("PATH", "").split(os.pathsep):
        if not path:
            continue
        full_path = os.path.join(path, argument)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return ""
