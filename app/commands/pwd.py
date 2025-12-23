""" A command that prints the current working directory """
import os

PWD_COMMAND = "pwd"

def command_pwd():
    """ Print the current working directory """
    print(os.getcwd())
