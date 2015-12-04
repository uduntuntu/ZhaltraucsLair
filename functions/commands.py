# -*- coding: utf-8 -*-

import functions.database as db
import functions.actions as action
import functions.conversations as conversation

commands = {
    'go': 2,
    'take': 2,
    'drop': 2,
    'use': 2,
    'jump': 1,
    'push': 2,
    'pull': 2,
    'talk': 2,
    'fight': 2,
    'help': 2,
    'menu': 1,
    'inventory': 1,
    'look': 2,
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


def execute(command, directions, items, npcs, player):
    '''
    :param command: only valid commands came in from isValid(command)
    :return: "main" if switch context to "main", "game" if keep playing.
    '''

    if command[0] == "go":
        go(command, directions, player)

    elif command[0] == "help":
        if len(command) == 1:
            help()

        else:
            help(command[1])

    elif command[0] == "menu":
        return "main"

    elif command[0] == "quit":
        raise SystemExit

    elif command[0] == "look":
        if len(command) == 1:
            look(items, npcs, player)
        else:
            look(items, npcs, player, command[1])

    elif command[0] == "take":
        if len(command) == 1:
            take(items)
        else:
            take(items, player, command[1])

    elif command[0] == "inventory":
        print(player.inventory)

    elif command[0] == "drop":
        if len(command) == 1:
            drop(player)
        else:
            drop(player, command[1])

    elif command[0] == "use":
        if len(command) == 1:
            use(player)
        else:
            use(player, command[1])

    elif command[0] == "jump":
        if player.roomID == 3:
            success = action.jump(player)
            if success == 2:
                db.updateRoomState(player.roomID, 2)
                if 'west' in directions:
                    db.updateMovements(player,
                                       'NULL', 'NULL', 4, 'NULL', 'NULL', 'NULL')
                    print(db.getRoomState(player.roomID))
                    db.updateRoomState(player.roomID, 1)
                else:
                    db.updateMovements(player,
                                       'NULL', 'NULL', 'NULL', 2, 'NULL', 'NULL')
                    print(db.getRoomState(player.roomID))
                    db.updateRoomState(player.roomID, 1)
            elif success == 1:
                db.updateRoomState(player.roomID, 3)
                db.modifyhp(-5)
                if 'west' in directions:
                    db.updateMovements(player,
                                       'NULL', 'NULL', 4, 'NULL', 'NULL', 'NULL')
                else:
                    db.updateMovements(player,
                                       'NULL', 'NULL', 'NULL', 2, 'NULL', 'NULL')
            else:
                db.updateRoomState(player.roomID, 4)
                print(db.getRoomState(player.roomID))
                raise SystemExit

        else:
            print("There is no reason to jump.")

    elif command[0] == "fight":
        if len(command) == 1:
            fight(player, npcs)
        else:
            fight(player, npcs, command[1])

    elif command[0] == "talk":
        if len(command) == 1:
            talk(player, npcs)
        else:
            talk(player, npcs, command[1])

    elif command[0] in commands:
        print('Command "{0:s}" is not implemented yet.'.format(command[0]))

    return "game"


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
        player = db.createPlayer()
        printRoomStateOrDescription(player)
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


def go(command, directions, player):
    if command[0] == "go" and len(command) == 1:
        print("You can go: ")
        for direction in directions.keys():
            print("\t* {}".format(direction))

    elif command[0] == "go" and len(command) == 2:
        if command[1] in directions:
            player.roomID = directions[command[1]]
            db.setPlayerRoomID(player.roomID)

            npcs = db.getNPCsInRoom(player.roomID)
            db.modifypoints(db.getPointsFromRoom(player.roomID))
            if player.roomID == 2 and 'torch' in player.inventory:
                for i in (2, 3, 5):
                    db.updateRoomState(i, 1)
                printRoomStateOrDescription(player)
            elif player.roomID in (3, 5) and 'torch' not in player.inventory:
                print(db.getRoomState(player.roomID))
                raise SystemExit
            elif player.roomID == 6 and npcs != {}:
                db.updateMovements(player,
                                   'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL')
                printRoomStateOrDescription(player)
            elif player.roomID == 7:
                success = action.throwIntelligence(player)
                if success == 2:
                    db.updateRoomState(player.roomID, 0)
                    printRoomStateOrDescription(player)
                elif success == 1:
                    db.updateRoomState(player.roomID, 1)
                    printRoomStateOrDescription(player)
                    db.modifyhp(-2)
                else:
                    db.updateRoomState(player.roomID, 2)
                    printRoomStateOrDescription(player)
                    db.modifyhp(-10)
            elif player.roomID == 8:
                success = action.throwIntelligence(player)
                if success in (1, 2):
                    db.updateRoomState(player.roomID, 0)
                    printRoomStateOrDescription(player)
                    db.updateMovements(player, 15, 7, 'NULL', 14, 'NULL', 'NULL')
                else:
                    db.updateRoomState(player.roomID, 1)
                    printRoomStateOrDescription(player)
            elif player.roomID == 13:
                printRoomStateOrDescription(player)
                for key, character in npcs.items():
                    if character.ID == 7:
                        npc = npcs[key]
                quest=conversation.talk(npc)
                if quest==1:
                    for key, character in npcs.items():
                        if character.ID == 21:
                            npc = key
                    fight(player,npcs,npc)
            elif player.roomID == 15:
                printRoomStateOrDescription(player)
                success = action.throwIntelligence(player)
                if success == 2:
                    db.updateRoomState(player.roomID, 0)
                    printRoomStateOrDescription(player)
                if success == 1:
                    db.updateRoomState(player.roomID, 1)
                    printRoomStateOrDescription(player)
                    db.modifyhp(-8)
                else:
                    db.updateRoomState(player.roomID, 2)
                    printRoomStateOrDescription(player)
                    print(db.getRoomState(player.roomID))
                    raise SystemExit

            elif player.roomID == 24:
                printRoomStateOrDescription(player)
                success = action.throwIntelligence(player)
                if success == 2:
                    db.updateRoomState(player.roomID, 0)
                    printRoomStateOrDescription(player)
                if success == 1:
                    db.updateRoomState(player.roomID, 1)
                    printRoomStateOrDescription(player)
                    db.modifyhp(-5)
                else:
                    db.updateRoomState(player.roomID, 2)
                    printRoomStateOrDescription(player)
                    db.modifyhp(-10)
            else:
                # print room state after room is actually changed
                printRoomStateOrDescription(player)

        else:
            print(
                "Invalid direction. You can use "
                "only directions in list below:"
            )
            for direction in directions.keys():
                print("\t* {}".format(direction))


def help(command=None):
    if command == None:
        print("List of available commands:")
        for c in commands.keys():
            print("\t* {0:s}".format(c))
        print('For more information, please write "help [command]".')

    elif command in commands:
        print('help for "{0:s}" is not implemented yet.'.format(command))

    else:
        print('No help for "{0:s}". It is an invalid command.'.format(command))


def look(items, npcs, player, object=None):
    if object == None:
        if items != []:
            print("There are following items in room:")
            for item in items:
                print("\t* {}".format(item))
        else:
            print("There are no items in room.")

        if npcs != {}:
            print("There are following NPCs in room to look at:")
            for key, npc in npcs.items():
                print("\t {} = {} {}".format(key, npc.NPCName, npc.ID))
        else:
            print("There are no NPCs in room.")

        if player.inventory != []:
            print("There are following items in inventory:")
            for item in player.inventory:
                print("\t* {}".format(item))
        else:
            print("There are no items in inventory.")

    elif object in items or object in npcs.keys() or object in player.inventory:
        if object in items:
            print(db.getItemDescription(object))
        elif object in npcs.keys():
            print(db.getNPCDescription(npcs[object]))
        elif object in player.inventory:
            print(db.getItemDescription(object))

    else:
        print('Item "{}" not found.'.format(object))


def take(items, player=None, item=None):
    if item == None:
        if items != []:
            print("You can take items below:")
            for item in items:
                print("\t* {}".format(item))
        else:
            print("There is no items in room.")
    elif item in items:
        db.pickItem(item, player)
        db.modifypoints(db.getPointsFromItem(item))
        print('You took item "{}".'.format(item))
        player.inventory.append(item)
    else:
        print('Cannot take item "{}".'.format(item))


def drop(player=None, item=None):
    if item == None:
        if player.inventory != []:
            print("You can drop items below:")
            for item in player.inventory:
                print("\t* {}".format(item))
        else:
            print("There is no items in inventory to drop.")
    elif item in player.inventory:
        db.dropItem(item, player)
        print('You dropped item "{}".'.format(item))
        player.inventory.remove(item)
    else:
        print('Cannot drop item "{}".'.format(item))


def use(player=None, item=None):
    if item == None:
        if player.inventory != []:
            print("You can use items below:")
            for item in player.inventory:
                print("\t* {}".format(item))
        else:
            print("There is no items in inventory to use.")

    elif item in player.inventory:
        print("Using item {} doesn't make sense.")

    else:
        print('Cannot use item "{}".'.format(item))


def fight(player=None, npcs={}, npc=None):
    if npc == None:
        print("Enemies you can attack:")
        for key, enemy in npcs.items():
            print("\t{} = {}".format(key, enemy.NPCName))

    elif npc in npcs.keys():
        enemyIsAlive = True
        while enemyIsAlive:
            # Attack turn
            attack = action.attack(player, npcs[npc])
            if attack != 0:
                print("You hit {} points.".format(-attack))
            else:
                print("You miss!")
            db.modifyNPCHP(attack, npcs[npc])
            npcs[npc] = db.updateNPC(npcs[npc])
            player = db.updatePlayer(player)
            # Dodge turn
            for npc in npcs.keys():
                npcs = db.getNPCsInRoom(player.roomID)
                if npc in npcs.keys():
                    if npcs[npc].HP > 0:
                        dodge = action.dodge(player, npcs[npc])
                        if dodge != 0:
                            print("You get {} points damage.".format(-dodge))
                        else:
                            print("You succeeded to dodge!")
                        db.modifyhp(dodge)
                        npcs[npc] = db.updateNPC(npcs[npc])
                        player = db.updatePlayer(player)
                        if player.HP <= 0:
                            print("You died.")
                            raise SystemExit

                if npc in npcs.keys():
                    if npcs[npc].HP <= 0:
                        print("{} {} died.".format(npcs[npc].NPCName, npcs[npc].ID))

                        db.modifypoints(db.getPointsFromNPC(npcs[npc].ID))
                        db.cleanDiedNPC(npcs[npc])
                        npcs = db.getNPCsInRoom(player.roomID)

                        enemyIsAlive = False
                        if player.roomID == 1:
                            db.updateMovements(player,
                                               2, 'NULL', 'NULL', 'NULL', 'NULL', 'NULL')
                        if player.roomID == 6 and npcs == {}:
                            db.updateMovements(player,
                                               'NULL', 'NULL', 5, 'NULL', 'NULL', 'NULL')
                            db.updateRoomState(player.roomID, 1)
                            printRoomStateOrDescription(player)
                        else:
                            db.updateRoomState(player.roomID, 2)


                        if player.roomID == 10:
                            db.updateRoomState(player.roomID, 2)
                            printRoomStateOrDescription(player)

    else:
        print('Cannot fight with "{}".'.format(npc))
        2


def talk(player, npcs, npc=None):
    if npc == None:
        if npcs != {}:
            print("Characters you can talk with:")
            for key, character in npcs.items():
                print("\t{} = {}".format(key, character.NPCName))
        else:
            print("There is no characters to talk with in room.")

    if npc in npcs.keys():
        quest = conversation.talk(npcs[npc])
        if quest == 1:
            db.updateMovements(player,
                               12, 9, 'NULL', 11, 'NULL', 'NULL')
            db.updateRoomState(player.roomID,4)
            db.modifyNPCHP(-1, npcs[npc])
            db.modifypoints(db.getPointsFromNPC(npcs[npc].ID))
            db.cleanDiedNPC(npcs[npc])
            npcs = db.getNPCsInRoom(player.roomID)
            printRoomStateOrDescription(player)


def printRoomStateOrDescription(player):
    # get and print room description or state
    roomState = db.getRoomState(player.roomID)
    if roomState is not None:
        print("--\n{}".format(roomState))
    else:
        roomDescription = db.getRoomDescription(player.roomID)
        print("--\n{}".format(roomDescription))
