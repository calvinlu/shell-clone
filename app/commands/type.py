"""
A command that checks whether a command is a builtin, an executable file, or unrecognized.
"""
TYPE_COMMAND = "type"

VALID_BUILTINS = ["echo", "type", "exit"]

def command_type(args: list[str]):
    """ Type the arguments """
    if len(args) == 0:
        print("type: missing operand")
        return
    argument = args[0]
    print(f"{argument} is a shell builtin" if argument in
     VALID_BUILTINS else f"{argument} not found")
