# -*- coding: utf-8 -*-

commands = {
    'go',
    'turn',
    'help',
    'exit'
}


def isValid(command):
    if command[0] in commands:
        return True
    else:
        return False


def go(direction):
    directions = {'left', 'right', 'front', 'up', 'down'}
    if len(direction) == 2 and direction[1] in directions:
        print(direction[1])
    elif(len(direction) == 1 and direction[0] == "turn"):
        print(direction[0])
    else:
        print("Invalid direction. You can use only directions in list below:")
        print(directions)


def help(*args):
    print("List of available commands:")
    print(commands)
