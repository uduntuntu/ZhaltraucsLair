# -*- coding: utf-8 -*-
""" Basic combat experiment. Rat vs. Conan the Barbarian."""
import random
def dice(slices):
    return random.randint(1,slices)

#BARBARIAN
barName=("Conan")
barHp=28
barS=18
barI=8
barA=2

#weapon is a short sword, no damage boost

#Leather, Chainmail; 1 armor, worn, 10 coins, 1 weight
barArmor=1

barBd=dice(10)+3
barPiercing=0

#RAT
# (d6 damage 1 piercing); 7 HP; 1 Armor
ratName="Cave Rat"
ratHp=7
ratArmor=0

ratBd=dice(6)
ratPiercing=1

def hit(ratHp):
    print(barName+" attacks the "+ratName+" !")
    diecast=barS+dice(10)
    if diecast>10:
        print (barName+" strikes the "+ratName+" succesfully!")
        attack=barBd-(ratArmor-barPiercing)
        ratHp-=attack
        attack=str(attack)
        print (barName+" does "+attack+" damage!")
        input(ratName+" shrieks in pain!")
        return ratHp

    if diecast==(7<9):
        print (barName+" strikes the "+ratName+" but the "+ratName+" counters!")
        attack=barBd/2-(ratArmor-barPiercing)
        ratHp-=attack
        attack=str(attack)
        print (barName+" does "+attack+" damage!")
        input(ratName+" shrieks in pain!")
        return ratHp




def combat(barHp,ratHp):
    print("Combat!")
    while ratHp>0 and barHp>0:
        (ratName+" attacks!")
        rollDefy=barA+dice(10)
        if rollDefy>=10:
            print(barName+" dodges!")
            ratHp=hit(ratHp)

        elif rollDefy==(7<9):
            print(barName+" partially dodges!")
            print(ratName+" does half damage!")
            input (barName+" grunts in pain!")
            hploss=ratBd/2-(barArmor+ratPiercing)
            barHp-=hploss
            print(barName+" loses "+hploss+" hitpoints!")
            input (barName+" howls in pain!")
            input(barName+" has "+barHp+" hitpoints left!")
            ratHp=hit(ratHp)
        else:
            print (ratName+" strikes the "+barName+" succesfully!")
            attack=ratBd-(barArmor-ratPiercing)
            barHp-=attack
            attack=str(attack)
            print (ratName+" does "+attack+" damage!")
            input (barName+" howls in pain!")
            ratHp=hit(ratHp)

    print(ratName+" has died!")


combat(barHp,ratHp)
