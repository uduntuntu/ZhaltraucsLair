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
    'quit': 1,
    'give': 2
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
                                       'NULL', 'NULL', 4, 'NULL', 'NULL',
                                       'NULL')
                    printRoomStateOrDescription(player)
                    db.updateRoomState(player.roomID, 1)

                else:
                    db.updateMovements(player,
                                       'NULL', 'NULL', 'NULL', 2, 'NULL',
                                       'NULL')
                    printRoomStateOrDescription(player)
                    db.updateRoomState(player.roomID, 1)

            elif success == 1:
                db.updateRoomState(player.roomID, 3)
                db.modifyhp(-5)
                if 'west' in directions:
                    db.updateMovements(player,
                                       'NULL', 'NULL', 4, 'NULL', 'NULL',
                                       'NULL')

                else:
                    db.updateMovements(player,
                                       'NULL', 'NULL', 'NULL', 2, 'NULL',
                                       'NULL')

            else:
                db.updateRoomState(player.roomID, 4)
                printRoomStateOrDescription(player)
                raise SystemExit

        elif player.roomID == 27:
            success = action.jump(player)
            if success == 2:
                db.updateRoomState(player.roomID, 1)
                if 'north' in directions:
                    db.updateMovements(player,
                                       'NULL',28,31,'NULL','NULL','NULL')
                    printRoomStateOrDescription(player)
                    db.updateRoomState(player.roomID, 0)
                else:
                    db.updateMovements(player,
                                       26, 'NULL', 'NULL', 'NULL', 'NULL',
                                       'NULL')
                    printRoomStateOrDescription(player)
                    db.updateRoomState(player.roomID, 0)

            elif success == 1:
                db.updateRoomState(player.roomID, 2)
                db.modifyhp(-5)
                if 'north' in directions:
                    db.updateMovements(player,
                                       'NULL',28,31,'NULL','NULL','NULL')
                    print(db.getRoomState(player.roomID))
                    db.updateRoomState(player.roomID, 0)

                else:
                    db.updateMovements(player,
                                       26, 'NULL', 'NULL', 'NULL', 'NULL',
                                       'NULL')
                    printRoomStateOrDescription(player)
            else:
                db.updateRoomState(player.roomID, 3)
                printRoomStateOrDescription(player)
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

    elif command[0] == "give":
        if len(command) == 1:
            give(player)
        else:
            give(player, command[1])

    elif command[0] == "push":
        if len(command) == 1:
            push(player)
        else:
            push(player, command[1])


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
        if directions != {}:
            print("You can go: ")
            for direction in directions.keys():
                print("\t* {}".format(direction))

        else:
            print("You can't go anywhere, try to do something else.")

    elif command[0] == "go" and len(command) == 2:
        # cheat for testing game
        roomID = []
        for i in range(1, 35):
            roomID.append(str(i))

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
                printRoomStateOrDescription(player)
                fight(player,npcs)

            elif player.roomID == 7:
                if db.getRoomStateID(player.roomID) != 3:
                    success = action.throwIntelligence(player)
                    if success == 2:
                        db.updateRoomState(player.roomID, 0)
                        printRoomStateOrDescription(player)
                        db.updateRoomState(player.roomID, 3)
                    elif success == 1:
                        db.updateRoomState(player.roomID, 1)
                        printRoomStateOrDescription(player)
                        db.modifyhp(-2)
                        db.updateRoomState(player.roomID, 3)
                    else:
                        db.updateRoomState(player.roomID, 2)
                        printRoomStateOrDescription(player)
                        db.modifyhp(-10)
                        db.updateRoomState(player.roomID, 3)

                else:
                    printRoomStateOrDescription(player)

            elif player.roomID == 8:
                success = action.throwIntelligence(player)
                if success in (1, 2):
                    db.updateRoomState(player.roomID, 0)
                    printRoomStateOrDescription(player)
                    db.updateMovements(player, 15, 7, 'NULL', 14, 'NULL',
                                       'NULL')
                else:
                    db.updateRoomState(player.roomID, 1)
                    printRoomStateOrDescription(player)

            elif player.roomID == 11:
                printRoomStateOrDescription(player)
                items = db.getItemsInRoom(player.roomID)
                if "sword" in items:
                    take(items, player, "sword")

            elif player.roomID == 12:
                printRoomStateOrDescription(player)
                fight(player,npcs)

            elif player.roomID == 13:
                printRoomStateOrDescription(player)
                if npcs != {}:
                    for key, character in npcs.items():
                        if character.ID == 7:
                            npc = npcs[key]
                    quest = conversation.talk(npc)
                    db.dropNPCItem(npc,"carddeck")
                    db.cleanNPCFromRoom(npc)
                    npcs = db.getNPCsInRoom(player.roomID)
                    if quest == 1:
                        fight(player, npcs)
                        db.updateRoomState(player.roomID, 3)
                        printRoomStateOrDescription(player)
                        items = db.getItemsInRoom(player.roomID)
                        if "carddeck" in items:
                            take(items, player, "carddeck")
                        db.updateRoomState(player.roomID, 1)
                        printRoomStateOrDescription(player)
                    if quest == 0:
                        db.updateRoomState(player.roomID, 2)
                        printRoomStateOrDescription(player)

            elif player.roomID == 15:
                if db.getRoomStateID(player.roomID) != 3:
                    success = action.throwIntelligence(player)
                    if success == 2:
                        db.updateRoomState(player.roomID, 0)
                        printRoomStateOrDescription(player)
                        db.updateRoomState(player.roomID, 3)
                    elif success == 1:
                        db.updateRoomState(player.roomID, 1)
                        printRoomStateOrDescription(player)
                        db.modifyhp(-8)
                        db.updateRoomState(player.roomID, 3)
                    else:
                        db.updateRoomState(player.roomID, 2)
                        print(db.getRoomState(player.roomID))
                        raise SystemExit

                else:
                    printRoomStateOrDescription(player)

            elif player.roomID == 17:
                printRoomStateOrDescription(player)
                if npcs != {}:
                    for key, character in npcs.items():
                        if character.ID == 8:
                            npc = npcs[key]
                    quest = conversation.talk(npc)
                    if quest == 1:
                        db.dropNPCItem(npc,"healthpotion")
                        db.cleanNPCFromRoom(npc)
                        npcs = db.getNPCsInRoom(player.roomID)
                        fight(player, npcs)
                        db.updateRoomState(player.roomID, 4)
                        printRoomStateOrDescription(player)
                        items = db.getItemsInRoom(player.roomID)
                        if "healthpotion" in items:
                            take(items, player, "healthpotion")
                        db.updateRoomState(player.roomID, 3)
                        printRoomStateOrDescription(player)
                    elif quest == 0:
                        keys = []
                        for key, npc in npcs.items():
                            keys.append(key)
                        for key in keys:
                            db.cleanNPCFromRoom(npcs[key])
                        db.updateRoomState(player.roomID, 3)
                        printRoomStateOrDescription(player)

            elif player.roomID == 19 \
                    and command[1] == "south" \
                    and "torch" in player.inventory:
                roomstate = db.getRoomStateID(18)
                if roomstate == 0:
                    player.roomID = 18
                    db.setPlayerRoomID(player.roomID)
                    db.updateRoomState(player.roomID,2)
                    for i in (23,24):
                        db.bringNPCToRoom(player.roomID,i)
                    npcs = db.getNPCsInRoom(player.roomID)
                    printRoomStateOrDescription(player)
                    fight(player,npcs)
                    db.updateRoomState(player.roomID,3)
                    printRoomStateOrDescription(player)
                else:
                    printRoomStateOrDescription(player)

            elif player.roomID == 21 \
                    and command[1] == "west" \
                    and player.playerClass == "barbarian":
                player.roomID = 20
                db.setPlayerRoomID(player.roomID)
                db.updateRoomState(player.roomID,1)
                db.updateMovements(player,19,'NULL','NULL','NULL','NULL','NULL')
                printRoomStateOrDescription(player)
                db.updateRoomState(player.roomID,0)
                printRoomStateOrDescription(player)

            elif player.roomID == 21 \
                    and command[1] == "east" \
                    and player.playerClass == "barbarian":
                player.roomID = 22
                db.setPlayerRoomID(player.roomID)
                db.updateMovements(player,23,'NULL','NULL','NULL','NULL',25)
                printRoomStateOrDescription(player)

            elif player.roomID == 22 \
                    and npcs != {} \
                    and "armor" in player.inventory \
                    and "carddeck" in player.inventory:
                if db.getRoomStateID(player.roomID) != 7:
                    db.updateRoomState(22, 2)
                    printRoomStateOrDescription(player)
                    db.updateRoomState(22, 3)
                    printRoomStateOrDescription(player)
                    db.updateRoomState(22, 7)
                    items = db.getItemsInRoom(player.roomID)
                    if "gold" in items:
                        take(items, player, "gold")
                        print("You now have a huge pile of gold in your inventory")

                else:
                    printRoomStateOrDescription(player)

            elif player.roomID == 22 \
                    and npcs != {} \
                    and "armor" in player.inventory:
                if db.getRoomStateID(player.roomID) not in (6,7):
                    db.updateRoomState(22, 2)
                    printRoomStateOrDescription(player)
                    success = action.throwIntelligence(player)
                    if success == 2:
                        db.updateRoomState(player.roomID, 3)
                        printRoomStateOrDescription(player)
                        db.updateRoomState(22, 7)
                        items = db.getItemsInRoom(player.roomID)
                        if "gold" in items:
                            take(items, player, "gold")
                            print("You now have a huge pile of gold in your inventory")

                    elif success != 2:
                        db.updateRoomState(player.roomID, 4)
                        printRoomStateOrDescription(player)
                        fight(player,npcs)
                        db.updateRoomState(player.roomID, 5)
                        printRoomStateOrDescription(player)
                        db.updateRoomState(22, 7)
                        items = db.getItemsInRoom(player.roomID)
                        if "gold" in items:
                            take(items, player, "gold")
                            print("You now have a huge pile of gold in your inventory")

                else:
                    printRoomStateOrDescription(player)

            elif player.roomID == 22 and npcs != {}:
                db.updateRoomState(22, 0)
                printRoomStateOrDescription(player)
                fight(player,npcs)
                db.updateRoomState(player.roomID, 5)
                printRoomStateOrDescription(player)
                db.updateRoomState(22, 7)
                items = db.getItemsInRoom(player.roomID)
                if "gold" in items:
                    take(items, player, "gold")
                    print("You now have a huge pile of gold in your inventory")

            elif player.roomID == 22 and npcs =={}:
                db.updateRoomState(22, 7)
                printRoomStateOrDescription(player)

            elif player.roomID == 23 and 'armor' in player.inventory:
                db.updateRoomState(player.roomID, 2)
                printRoomStateOrDescription(player)

            elif player.roomID == 24:
                success = action.throwIntelligence(player)
                if success == 2:
                    db.updateRoomState(player.roomID, 0)
                    printRoomStateOrDescription(player)
                elif success == 1:
                    db.updateRoomState(player.roomID, 1)
                    printRoomStateOrDescription(player)
                    db.modifyhp(-5)
                else:
                    db.updateRoomState(player.roomID, 2)
                    printRoomStateOrDescription(player)
                    db.modifyhp(-10)

            elif player.roomID == 32 \
                    and command[1] == "east" \
                    and player.playerClass == "barbarian":
                player.roomID = 31
                db.setPlayerRoomID(player.roomID)
                db.updateRoomState(player.roomID,1)
                db.updateMovements(player,'NULL',34,'NULL',27,'NULL','NULL')
                printRoomStateOrDescription(player)
                db.updateRoomState(player.roomID,0)
                printRoomStateOrDescription(player)

            elif player.roomID == 33 \
                    and command[1] == "south" \
                    and player.playerClass == "thief":
                db.updateRoomState(player.roomID, 2)
                printRoomStateOrDescription(player)

            elif player.roomID == 33 and npcs != {}:
                printRoomStateOrDescription(player)
                npcs = db.getNPCsInRoom(player.roomID)
                fight(player,npcs)

            else:
                # print room state after room is actually changed
                printRoomStateOrDescription(player)

        # cheat for testing game
        elif command[1] in roomID:
            player.roomID = int(command[1])
            db.setPlayerRoomID(player.roomID)
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

    elif item == 'armor':
        db.updateRoomState(player.roomID, 1)
        print(printRoomStateOrDescription(player))
        db.updateRoomState(player.roomID, 2)
        db.takeItem(item, player)
        db.modifypoints(db.getPointsFromItem(item))



    elif item in items:
        db.takeItem(item, player)
        db.modifypoints(db.getPointsFromItem(item))
        print('You took item "{}".'.format(item))
        player.inventory.append(item)
        if item == "torch" and player.roomID == 18:
            db.updateRoomState(player.roomID,0)
            printRoomStateOrDescription(player)


        elif player.roomID == 30 and item=="gold" and item in player.inventory:
            db.updateRoomState(player.roomID, 5)
            printRoomStateOrDescription(player)
            raise SystemExit

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
        if player.roomID == 18 and item == "torch":
            db.updateRoomState(player.roomID,1)
            printRoomStateOrDescription(player)

        elif player.roomID == 30 and item == "gold":
            db.updateRoomState(player.roomID,1)
            npcs = db.getNPCsInRoom(player.roomID)
            for key, character in npcs.items():
                if character.ID == 17:
                    npc = npcs[key]
            if player.playerClass == "barbarian":
                db.dropNPCItem(npc,"shield")
                items = db.getItemsInRoom(player.roomID)
                take(items,player,"shield")

            else:
                db.dropNPCItem(npc,"sleepingpotion")
                items = db.getItemsInRoom(player.roomID)
                take(items,player,"sleepingpotion")

            db.updateRoomState(player.roomID,3)
            printRoomStateOrDescription(player)
            db.updateRoomState(player.roomID,4)

    else:
        print('Cannot drop item "{}".'.format(item))


def use(player, item=None):
    roomState = db.getRoomStateID(player.roomID)
    if item == None:
        if player.inventory != []:
            print("You can use items below:")
            for item in player.inventory:
                print("\t* {}".format(item))
        else:
            print("There is no items in inventory to use.")

    elif item == "torch" and item in player.inventory and player.roomID == 21:
        db.updateRoomState(player.roomID, 2)
        printRoomStateOrDescription(player)
        npcs = db.getNPCsInRoom(player.roomID)
        keys = []
        for key in npcs.keys():
            keys.append(key)
        for key in keys:
            db.cleanNPCFromRoom(npcs[key])
        db.updateMovements(player,'NULL','NULL',20,22,'NULL','NULL')
        db.updateRoomState(22,6)

    elif item == "sleepingpotion" and item in player.inventory and player.roomID == 33 and roomState==2:
        db.updateRoomState(player.roomID, 3)
        player.inventory.remove(item)
        printRoomStateOrDescription(player)
        npcs = db.getNPCsInRoom(player.roomID)
        keys = []
        for key in npcs.keys():
            keys.append(key)
        for key in keys:
            db.cleanNPCFromRoom(npcs[key])
        raise SystemExit

    elif item == "healthpotion" and item in player.inventory:
        db.modifyhp(15)
        player = db.updatePlayer(player)
        player.inventory.remove(item)
        db.useItem(item)
        print("You drink the health potion. You feel reinvigorated as the "
              "healing potion surges through your body, mending the wounds "
              "and restoring your beaten physique."
              )

    elif item in player.inventory:
        print('''Using item "{}" doesn't make sense.'''.format(item))

    else:
        print('Cannot use item "{}".'.format(item))


def fight(player=None, npcs={}, npc=None):
    if npc == None:
        while npcs != {}:
            for i in range(0,len(npcs)):
                npcs = fight(player,npcs,'0')

    elif npcs[npc].NPCName=='Dragon':
        db.updateRoomState(player.roomID, 2)
        printRoomStateOrDescription(player)
        raise SystemExit

    elif npcs[npc].NPCName=='Spider':
        db.updateRoomState(player.roomID, 1)
        printRoomStateOrDescription(player)
        raise SystemExit

    elif npcs[npc].NPCName == "Zhaltrauc":
        shieldIsActive = False
        useShield = input("The gem on Zhaltrauc's crown begins to glow!")
        if useShield.lower() == "use shield" and "shield" in player.inventory:
            shieldIsActive=True
            print("Zhaltrauc shoot's a beam of light from his gem. You lift "
                  "your shield just in time and deflect the shot, blinding "
                  "Zhaltrauc!")
        else:
            print("Blinding light flashes from Zhaltrauc's gem! You are blinded by the light!")

        # Attack turn
        if shieldIsActive:
            attack = action.attack(player, npcs[npc])
            db.modifyNPCHP(attack, npcs[npc])
            npcs[npc] = db.updateNPC(npcs[npc])
            player = db.updatePlayer(player)
            if npcs[npc].HP <= 0:
                print("{} {} died.".format(npcs[npc].NPCName,
                                           npcs[npc].ID))

                db.modifypoints(db.getPointsFromNPC(npcs[npc].ID))
                db.cleanNPCFromRoom(npcs[npc])
                npcs = db.getNPCsInRoom(player.roomID)
                db.updateRoomState(player.roomID,1)
                printRoomStateOrDescription(player)
                raise SystemExit

        # Dodge turn
        if not shieldIsActive:
            if npcs[npc].HP > 0:
                dodge = action.dodge(player, npcs[npc])
                db.modifyhp(dodge)
                npcs[npc] = db.updateNPC(npcs[npc])
                player = db.updatePlayer(player)
                if player.HP <= 0:
                    print("You died.")
                    raise SystemExit

    elif npc in npcs.keys():
        enemyIsAlive = True
        while enemyIsAlive:
            # Attack turn
            attack = action.attack(player, npcs[npc])
            db.modifyNPCHP(attack, npcs[npc])
            npcs[npc] = db.updateNPC(npcs[npc])
            player = db.updatePlayer(player)
            input('Press "Enter"')
            # Dodge turn
            for npc in npcs.keys():
                npcs = db.getNPCsInRoom(player.roomID)
                if npc in npcs.keys():
                    if npcs[npc].HP > 0:
                        dodge = action.dodge(player, npcs[npc])
                        db.modifyhp(dodge)
                        npcs[npc] = db.updateNPC(npcs[npc])
                        player = db.updatePlayer(player)
                        if player.HP <= 0:
                            print("You died.")
                            raise SystemExit

                if npc in npcs.keys():
                    if npcs[npc].HP <= 0:
                        print("{} {} died.".format(npcs[npc].NPCName,
                                                   npcs[npc].ID))

                        db.modifypoints(db.getPointsFromNPC(npcs[npc].ID))
                        db.cleanNPCFromRoom(npcs[npc])
                        npcs = db.getNPCsInRoom(player.roomID)

                        enemyIsAlive = False
                        if player.roomID == 1:
                            db.updateMovements(player,
                                               2, 'NULL', 'NULL', 'NULL',
                                               'NULL', 'NULL')

                        if player.roomID == 6 and npcs == {}:
                            db.updateMovements(player,
                                               'NULL', 'NULL', 5, 'NULL',
                                               'NULL', 'NULL')
                            db.updateRoomState(player.roomID, 1)
                            printRoomStateOrDescription(player)
                            db.updateRoomState(player.roomID, 2)

                        if player.roomID == 10:
                            db.updateRoomState(player.roomID, 2)
                            printRoomStateOrDescription(player)

                        if player.roomID == 12 and npcs == {}:
                            db.updateMovements(player,
                                               'NULL', 10, 13, 'NULL', 'NULL',
                                               'NULL')
                            db.updateRoomState(player.roomID, 1)
                            printRoomStateOrDescription(player)
                            db.updateRoomState(player.roomID, 2)

                input('Press "Enter"')

    else:
        print('Cannot fight with "{}".'.format(npc))

    return npcs

def talk(player, npcs, npc=None):
    if npc == None:
        if npcs != {}:
            print("Characters you can talk with:")
            for key, character in npcs.items():
                print("\t{} = {}".format(key, character.NPCName))
        else:
            print("There are no characters to talk with in room.")

    if npc in npcs.keys():
        if player.roomID == 10:
            quest = conversation.talk(npcs[npc])
            if quest == 1:
                db.updateMovements(player,
                                   12, 9, 'NULL', 11, 'NULL', 'NULL')
                db.updateRoomState(player.roomID, 4)
                db.modifypoints(db.getPointsFromNPC(npcs[npc].ID))
                db.cleanNPCFromRoom(npcs[npc])
                npcs = db.getNPCsInRoom(player.roomID)
                printRoomStateOrDescription(player)

        elif player.roomID == 34:
            quest = conversation.talk(npcs[npc], player)
            if quest == 1:
                db.updateMovements(player,
                                   31, 33, 'NULL', 'NULL', 'NULL', 'NULL')
                db.updateRoomState(player.roomID, 1)

        else:
            print("Conversation with {} has not written yet.".format(
                npcs[npc].NPCName))


def give(player, item=None):
    npcs = db.getNPCsInRoom
    if item == None:
        if player.inventory != []:
            print("You can give items below:")
            for item in player.inventory:
                print("\t* {}".format(item))
        else:
            print("You don't have any items to give!")

    elif item in player.inventory and npcs != {}:
        drop(player, item)

    elif item in player.inventory:
        print("There is no one to give anything.")

    else:
        print("You don't have item {}".format(item))


def push(player, item=None):
    if item == None:
        if player.roomID == 27:
            print("You can push a pillar.")
        else:
            print("You cannot push anything in this room.")

    elif player.roomID == 27 and item == "pillar":
        if player.playerClass == "barbarian":
            db.updateRoomState(player.roomID,4)
            printRoomStateOrDescription(player)
            db.updateMovements(player,
                               26,28,31,'NULL','NULL','NULL')
            db.updateRoomState(player.roomID,6)

        else:
            db.updateRoomState(player.roomID,5)
            printRoomStateOrDescription(player)
            db.updateRoomState(player.roomID,0)
            printRoomStateOrDescription(player)

def printRoomStateOrDescription(player):
    # get and print room description or state
    roomState = db.getRoomState(player.roomID)
    if roomState is not None:
        print("--\n{}".format(roomState))
    else:
        roomDescription = db.getRoomDescription(player.roomID)
        print("--\n{}".format(roomDescription))
