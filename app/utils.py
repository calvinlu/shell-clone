"""
A collection of utility functions for the shell.
"""
import os

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
