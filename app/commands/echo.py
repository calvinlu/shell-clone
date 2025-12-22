"""
A simple echo command that prints the arguments to the console.
"""

ECHO_COMMAND = "echo"

def command_echo(args: list[str]):
    """ Echo the arguments """
    print(" ".join(args))
