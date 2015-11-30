# -*- coding: utf-8 -*-
import random

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