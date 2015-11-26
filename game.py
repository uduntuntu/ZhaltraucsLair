# -*- coding: utf-8 -*-

import functions.commands as command
import functions.database as db

f = open('ASCII/StartScreen_UTF-8.asc', 'r')
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

        # update player object and if doesn't exest yet create it
        player = db.getPlayer()

        # get and print room description
        roomDescription = db.getRoomDescription(player.roomID)
        print("--\n{}".format(roomDescription))

        # get and print directions player can go
        directions = db.getDirections(player.roomID)
        print("Directions you can go:")
        for direction in directions.keys():
            print("\t* {}".format(direction))

        #
        c = input(prompt).lower().split()

        if (command.isValid(c)):
            context = command.execute(c, directions)
        else:
            print('Invalid command. '
                'Write "help" to get list of available commands.'
            )
