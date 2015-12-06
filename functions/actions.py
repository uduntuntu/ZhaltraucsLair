# -*- coding: utf-8 -*-
import random
import functions.database as db


def dice(slices):
    return random.randint(1, slices)


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
    # Player base damage
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

    playerWeapon = db.getPlayerWeapon(player)

    # NPC dodge skills
    if npc.agility >= 18:
        npcDS = 3

    elif npc.agility >= 16:
        npcDS = 2

    elif npc.agility >= 13:
        npcDS = 1

    elif npc.agility >= 9:
        npcDS = 0

    elif npc.agility >= 6:
        npcDS = -1

    elif npc.agility >= 4:
        npcDS = -2

    else:
        npcDS = -3

    npcArmor = db.getNPCArmor(npc)

    # Stats assigned, let's start to attack
    print("{}'s turn to attack.".format(player.playerName))

    hit = playerBD + dice(10)
    dodge = npcDS + dice(10)

    if hit >= 8:
        print("{} hits successfully!".format(player.playerName))
        return -(hit + playerWeapon - npcArmor)

    elif hit >= 5:
        if dodge >= 8:
            print("{} hits well but {} dodges!".format(player.playerName,
                                                       npc.NPCName))
            return 0
        elif dodge >= 5:
            print("{} hits well but {} can dodge a little bit.".format(
                player.playerName, npc.NPCName
            )
            )
            return -round((hit + playerWeapon - npcArmor) / 2)
        else:
            print("{} hits well.".format(player.playerName))
            return -(hit + playerWeapon - npcArmor)

    else:
        print ("{} misses.".format(player.playerName))
        return 0


def dodge(player, npc):
    # Player dodge skills
    if player.agility >= 18:
        playerDS = 3

    elif player.agility >= 16:
        playerDS = 2

    elif player.agility >= 13:
        playerDS = 1

    elif player.agility >= 9:
        playerDS = 0

    elif player.agility >= 6:
        playerDS = -1

    elif player.agility >= 4:
        playerDS = -2

    else:
        playerDS = -3

    playerArmor = db.getPlayerArmor(player)

    # NPC base damage
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

    npcWeapon = db.getNPCWeapon(npc)

    #stats assigned, let's start to counter-attack
    print("{} {}'s turn to attack.".format(npc.NPCName, npc.ID))
    hit = npcBD + dice(8)
    dodge = playerDS + dice(10)

    if hit >= 8:
        print("{} hits successfully.".format(npc.NPCName))
        return -(hit + npcWeapon - playerArmor)

    elif hit >= 5:
        if dodge >= 8:
            print("{} hits well but {} dodges!".format(npc.NPCName,
                                                       player.playerName))
            return 0
        elif dodge >= 5:
            print("{} hits well but {} can dodge a little bit!".format(
                npc.NPCName,player.playerName
            )
            )
            return -round((hit + npcWeapon - playerArmor) / 2)
        else:
            print("{} hits well.".format(npc.NPCName))
            return -(hit + npcWeapon - playerArmor)

    else:
        print("{} misses.".format(npc.NPCName))
        return 0
