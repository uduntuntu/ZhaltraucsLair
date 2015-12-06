# -*- coding: utf-8 -*-

import functions.commands as command
import functions.database as db

if db.testConnection():
    player = db.getPlayer()

f = open('ASCII/StartScreen_UTF-8.asc', 'r')
print(f.read())
f.close()

roomState = db.getRoomState(player.roomID)
if roomState is not None:
    print("--\n{}".format(roomState))
else:
    roomDescription = db.getRoomDescription(player.roomID)
    print("--\n{}".format(roomDescription))

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
        hp=db.gethp()
        points=db.getPointsFromPlayer()
        # update player object and if doesn't exist yet create it
        player = db.updatePlayer(player)

        print("\nYour HP: {}".format(hp) )
        print("Your points: {}".format(points))

        # get directions player can go
        directions = db.getDirections(player.roomID)

        # get items in room player can take
        items = db.getItemsInRoom(player.roomID)

        # get NPCs in room player can action (talk or fight)
        npcs = db.getNPCsInRoom(player.roomID)

        # ask a command from player
        c = input(prompt).lower().split()

        # pass a command, possible directions, items in room and the player
        # object to command parser
        if (command.isValid(c)):
            context = command.execute(c, directions, items, npcs, player)
        else:
            print('Invalid command. '
                'Write "help" to get list of available commands.'
            )
