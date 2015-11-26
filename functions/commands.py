# -*- coding: utf-8 -*-

import functions.database as db

commands = {
    'go': 2,
    'pick': 2,
    'drop': 2,
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

menu = {
    1: 'Start a new game.',
    2: 'Continue playing.',
    3: 'Load a saved game.',
    4: 'Save a game.',
    5: 'Quit game'
}


def isValid(command):
    if len(command) == 0:
        return False
    elif command[0] in commands and len(command) <= commands[command[0]]:
        return True
    else:
        return False


def execute(command, directions):
    '''
    :param command: only valid commands came in from isValid(command)
    :return: "main" if switch context to "main", "game" if keep playing.
    '''

    if command[0] == "go":
        go(command, directions)

    elif command[0] == "help":
        if len(command) == 1:
            help()

        else:
            help(command[1])

    elif command[0] == "menu":
        return "main"

    elif command[0] == "quit":
        raise SystemExit

    elif command[0] in commands:
        print('Command "{0:s}" is not implemented yet.'.format(command[0]))

    return "game"


def go(command, directions):
    if command[0] == "go" and len(command) == 1:
        print("You can go: ")
        for direction in directions.keys():
                print("\t* {}".format(direction))

    elif command[0] == "go" and len(command) == 2:
        if command[1] in directions:
            print(
                'moving to "{0:s}" '
                'is not implemented yet.'.format(command[1])
            )

        else:
            print(
                "Invalid direction. You can use "
                "only directions in list below:"
            )
            for direction in directions.keys():
                print("\t* {}".format(direction))


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
    '''
    :param selection: int 1-5
    :return: "main" if keep context to "main", "game" if switch to playing.
    '''

    if selection == 0:
        print("--\nMain menu:")
        for key, value in menu.items():
            print("{} = {}".format(key, value))
        return "main"

    elif selection == 1:
        db.initializeDatabase()
        db.populateTables()
        db.createPlayer()
        return "game"

    elif selection == 2:
        return "game"

    elif selection == 5:
        raise SystemExit

    elif selection in menu:
        print("Menu item {0} not implemented yet.".format(selection))
        return "main"

    else:
        for key, value in menu.items():
            print("{} = {}".format(key, value))
        raise ValueError('Invalid selection {0:d}.'.format(selection))