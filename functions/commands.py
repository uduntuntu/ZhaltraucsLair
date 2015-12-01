# -*- coding: utf-8 -*-

import functions.database as db
import functions.actions as action

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
            look(items, npcs)
        else:
            look(items, npcs, command[1])

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
                db.updateRoomState(player.roomID,2)
                if 'west' in directions:
                    db.updateMovements(player,'NULL','NULL',4,'NULL','NULL','NULL')
                    print(db.getRoomState(player.roomID))
                    db.updateRoomState(player.roomID,1)
                else:
                    db.updateMovements(player,'NULL','NULL','NULL',2,'NULL','NULL')
                    print(db.getRoomState(player.roomID))
                    db.updateRoomState(player.roomID,1)
            elif success == 1:
                db.updateRoomState(player.roomID,3)
                db.modifyhp(-5)
                if 'west' in directions:
                    db.updateMovements(player,'NULL','NULL',4,'NULL','NULL','NULL')
                else:
                    db.updateMovements(player,'NULL','NULL','NULL',2,'NULL','NULL')
            else:
                db.updateRoomState(player.roomID,4)
                print(db.getRoomState(player.roomID))
                raise SystemExit
        else:
            print("There is no reason to jump.")

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


def go(command, directions, player):
    if command[0] == "go" and len(command) == 1:
        print("You can go: ")
        for direction in directions.keys():
                print("\t* {}".format(direction))

    elif command[0] == "go" and len(command) == 2:
        if command[1] in directions:
            player.roomID = directions[command[1]]
            db.setPlayerRoomID(player.roomID)
            if player.roomID == 2 and 'torch' in player.inventory:
                for i in (2,3,5):
                    db.updateRoomState(i,1)
            elif player.roomID in (3,5) and 'torch' not in player.inventory:
                print(db.getRoomState(player.roomID))
                raise SystemExit
            elif player.roomID == 7:
                success = action.throwIntelligence(player)
                if success == 2:
                    db.updateRoomState(player.roomID,0)
                elif success == 1:
                    db.updateRoomState(player.roomID,1)
                    db.modifyhp(-2)
                else:
                    db.updateRoomState(player.roomID,2)
                    db.modifyhp(-10)
            elif player.roomID == 8:
                success = action.throwIntelligence(player)
                if success in (1,2):
                    db.updateRoomState(player.roomID,0)
                    db.updateMovements(player,15,7,'NULL',14,'NULL','NULL')
                else:
                    db.updateRoomState(player.roomID,1)
            elif player.roomID == 15:
                success = action.throwIntelligence(player)
                if success == 2:
                    db.updateRoomState(player.roomID,0)
                if success == 1:
                    db.updateRoomState(player.roomID,1)
                    db.modifyhp(-8)
                else:
                    db.updateRoomState(player.roomID,2)
                    print(db.getRoomState(player.roomID))
                    raise SystemExit

            elif player.roomID == 24:
                success = action.throwIntelligence(player)
                if success == 2:
                    db.updateRoomState(player.roomID,0)
                if success == 1:
                    db.updateRoomState(player.roomID,1)
                    db.modifyhp(-5)
                else:
                    db.updateRoomState(player.roomID,2)
                    db.modifyhp(-10)

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


def look(items,npcs, object=None):
    if object == None:
        if items != []:
            print("There are following items in room:")
            for object in items:
                print("\t* {}".format(object))
        else:
            print("There are no items in room.")

        if npcs !={}:
            print("There are following NPCs in room to look at:")
            for key, npc in npcs.items():
                print("\t {}={}".format(key, npc))
        else:
            print("There are no NPCs in room.")

    elif object in items or object in npcs.keys():
        if object in items:
            print(db.getItemDescription(object))
        elif object in npcs.keys():
            print(db.getNPCDescription(npcs[object]))
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
        db.pickItem(item,player)
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
        db.dropItem(item,player)
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
