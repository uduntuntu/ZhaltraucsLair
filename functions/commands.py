# -*- coding: utf-8 -*-

import functions.database as db

commands = {
    'go': 2,
    'turn': 1,
    'pick': 2,
    'use': 2,
    'push': 2,
    'pull': 2,
    'talk': 2,
    'fight': 2,
    'help': 2,
    'menu': 1,
    'inventory': 1,
    'look': 1,
    'quit': 1
}

directions = (
    'left',
    'right',
    'front',
    'up',
    'down'
)

menu = {
    1: 'Start a new game.',
    2: 'Continue playing.',
    3: 'Load a saved game.',
    4: 'Save a game.',
    5: 'Quit game'
}


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
    elif command[0] in commands:
        print('Command "{0:s}" is not implemented yet.'.format(command[0]))


def go(command):
    if command[0] == "go" and len(command) == 1:
        print("go", directions)
    elif command[0] == "go" and len(command) == 2:
        if command[1] in directions:
            print('moving to direction "{0:s}" '
                  'is not implemented yet.'.format(command[1])
                  )
        else:
            print("Invalid direction. You can use "
                  "only directions in list below:"
                  )
            print("go", directions)
    elif len(command) == 1 and command[0] == "turn":
        print('Turning around is not implemented yet.')


def help(command="none"):
    if command == "none":
        print("List of available commands:")
        for c in commands.keys():
            print("\t* {0:s}".format(c))
        print('For more information, please write "help [command]".')
    elif command in commands:
        print('help for "{0:s}" is not implemented yet.'.format(command))
    else:
        print('No help for "{0:s}". It is an invalid command.'.format(command))


def doMenu(selection=0):
    if selection == 0:
        print("Main menu:")
        for key, value in menu.items():
            print("{} = {}".format(key, value))
    elif selection == 1:
        db.initializeDatabase()
    elif selection == 2:
        pass
    elif selection == 5:
        raise SystemExit
    elif selection in menu:
        print("Menu item {0} not implemented yet.".format(selection))
    else:
        for key, value in menu.items():
            print("{} = {}".format(key, value))
        raise ValueError('Invalid selection {0:d}.'.format(selection))
