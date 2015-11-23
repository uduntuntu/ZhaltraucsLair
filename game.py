# -*- coding: utf-8 -*-

import functions.commands as command

prompt = ">>> "
view = {
    '0.0' : "Tutorial. You see a rat attacking you, fight!",
    '1.0' : "You stand in a start of dungeon. You see a torch."
}

position = '1.0'

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
        prompt = "(game) >>> "

        print("--\n{}".format(view[position]))
        c = input(prompt).lower().split()

        if (command.isValid(c)):
            context = command.execute(c)
        else:
            print('Invalid command. '
                'Write "help" to get list of available commands.'
            )

