# -*- coding: utf-8 -*-

import functions.commands as command
import functions.database as db

f = open('ASCII/otsikko_unicode.asc', 'r')
print(f.read())
f.close()


while True:
    '''
    You can end loop by selecting 5 in main context or write
    "quit" in game context.
    '''

    context = command.doMenu()

    while context == "main":
        prompt = "(main) >>> "
        try:
            c = int(input(prompt))
            context = command.doMenu(c)
        except ValueError as e:
            print(e)

    while context == "game":
        position = db.getPosition()
        prompt = "(game) >>> "

        print("--\n{}".format(position))
        c = input(prompt).lower().split()

        if (command.isValid(c)):
            context = command.execute(c)
        else:
            print('Invalid command. '
                'Write "help" to get list of available commands.'
            )
