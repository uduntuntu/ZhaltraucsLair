# -*- coding: utf-8 -*-

commands = (
    'go',
    'turn',
    'help',
    'exit'
)


def isValid(command):
    if command[0] in commands:
        return True
    else:
        return False


def execute(command):
    if command[0] in ("go", "turn"):
        go(command)
    elif command[0] == "help":
        help()


def go(direction):
    directions = ('left', 'right', 'front', 'up', 'down')
    if direction[0] == "go" and len(direction) == 2:
        if direction[1] in directions:
            print(direction)
        else:
            print("Invalid direction. You can use only directions in list below:")
            print(directions)
    elif direction[0] == "turn" and len(direction) == 1:
        print(direction)
    else:
        print('Invalid command. Write "help" to get full list of commands.')


def help():
    print("List of available commands:")
    print(commands)