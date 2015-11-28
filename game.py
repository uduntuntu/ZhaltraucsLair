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
        # validate to player that we are in correct context
        prompt = "(main) >>> "
        try:
            # in main menu context we catch only integers as commands
            c = int(input(prompt))
            context = command.doMenu(c)
        except ValueError as e:
            print(e)

    while context == "game":
        # validate to player that we are in correct context
        prompt = "(game) >>> "

        # update player object and if doesn't exist yet create it
        player = db.getPlayer()

        # get and print room description or state
        roomState = db.getRoomState(player.roomID)
        if roomState is not None:
            print("--\n{}".format(roomState))
        else:
            roomDescription = db.getRoomDescription(player.roomID)
            print("--\n{}".format(roomDescription))


        # get directions player can go
        directions = db.getDirections(player.roomID)

        # get items in room player can pick
        items = db.getItemsInRoom(player.roomID)

        # ask a command from player
        c = input(prompt).lower().split()

        # pass a command, possible directions, items in room and the player
        # object to command parser
        if (command.isValid(c)):
            context = command.execute(c, directions, items, player)
        else:
            print('Invalid command. '
                'Write "help" to get list of available commands.'
            )
