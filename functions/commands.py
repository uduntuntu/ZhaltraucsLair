# -*- coding: utf-8 -*-

commands = {
    'go' : 2,
    'turn' : 1,
    'help' : 2,
    'exit' : 1
}

directions = (
    'left',
    'right',
    'front',
    'up',
    'down'
)


def isValid(command):
    if command[0] in commands and len(command) <= commands[command[0]]:
        return True
    else:
        return False


def execute(command):
    if command[0] in ("go", "turn"):
        go(command)
    elif command[0] == "help":
        if len(command) == 1:
            help()
        else:
            help(command[1])


def go(command):
    if command[0] == "go" and len(command) == 1:
        print("go", directions)
    elif command[0] == "go" and len(command) == 2:
        if command[1] in directions:
            print(command)
        else:
            print(
                "Invalid direction. You can use only directions in list below:"
            )
            print(directions)
    elif len(command) == 1 and command[0] == "turn":
        print(command)

def help(command="none"):
    if command == "none":
        print("List of available commands:")
        print(commands.keys())
    elif command in commands:
        print(command)
    else:
        print('No help for "{0:s}".'.format(command))