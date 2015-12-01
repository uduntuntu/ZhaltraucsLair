# -*- coding: utf-8 -*-
import random
import functions.database as db

def dice(slices):
    return random.randint(1,slices)

def jump(player):
    throw = dice(10)
    if player.agility + throw >= 12:
        return 2
    elif player.agility + throw >= 10:
        return 1
    else:
        return 0


def throwIntelligence(player):
    throw = dice(10)
    if player.intelligence + throw >= 12:
        return 2
    elif player.intelligence + throw >= 10:
        return 1
    else:
        return 0


def throwAgility(player):
    throw = dice(10)
    if player.agility + throw >= 12:
        return 2
    elif player.agility + throw >= 10:
        return 1
    else:
        return 0

def attack(player, npc):
    playerHP = player.HP

    if player.strength >= 18:
        playerBD = 3

    elif player.strength >= 16:
        playerBD = 2

    elif player.strength >= 13:
        playerBD = 1

    elif player.strength >= 9:
        playerBD = 0

    elif player.strength >= 6:
        playerBD = -1

    elif player.strength >= 4:
        playerBD = -2

    else:
        playerBD = -3

    playerArmor = db.getPlayerArmor(player)
    playerWeapon = db.getPlayerWearpon(player)

    npcHP = npc.HP

    if npc.strength >= 18:
        npcBD = 3

    elif npc.strength >= 16:
        npcBD = 2

    elif npc.strength >= 13:
        npcBD = 1

    elif npc.strength >= 9:
        npcBD = 0

    elif npc.strength >= 6:
        npcBD = -1

    elif npc.strength >= 4:
        npcBD = -2

    else:
        npcBD = -3

    npcArmor = db.getNPCArmor(npc)

