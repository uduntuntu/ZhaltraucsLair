# coding=cp1252
import math
import random
noppa=random.randrange(1,11,1)

#BARBAARI
barNimi=("Counän")
barHp=28
barS=18
barI=8
barA=2

#weapon is a short sword, no damage boost

#Leather, Chainmail; 1 armor, worn, 10 coins, 1 weight
barArmor=1

barBd=random.randrange(1,11,1)+3
barPiercing=0

#ROTTA
# (d6 damage 1 piercing); 7 HP; 1 Armor
rotNimi="Cave Rat"
rotHp=7
rotArmor=0

rotBd=random.randrange(1,7,1)
rotPiercing=1

def lyönti(rotHp):
    print(barNimi+" attacks the "+rotNimi+" !")
    diecast=barS+noppa
    if diecast>10:
        print (barNimi+" strikes the "+rotNimi+" succesfully!")
        isku=barBd-(rotArmor-barPiercing)
        rotHp-=isku
        isku=str(isku)
        print (barNimi+" does "+isku+" damage!")
        input(rotNimi+" shrieks in pain!")
        return rotHp

    if diecast==(7<9):
        print (barNimi+" strikes the "+rotNimi+" but the "+rotNimi+" counters!")
        isku=barBd/2-(rotArmor-barPiercing)
        rotHp-=isku
        isku=str(isku)
        print (barNimi+" does "+isku+" damage!")
        input(rotNimi+" shrieks in pain!")
        return rotHp




def taistelu(barHp,rotHp):
    print("Combat!")
    while rotHp>0 and barHp>0:
        (rotNimi+" attacks!")
        rollDefy=barA+noppa
        if rollDefy>=10:
            print(barNimi+" dodges!")
            rotHp=lyönti(rotHp)

        elif rollDefy==(7<9):
            print(barNimi+" partially dodges!")
            print(rotNimi+" does half damage!")
            input (barNimi+" grunts in pain!")
            hploss=rotBd/2-(barArmor+rotPiercing)
            barHp-=hploss
            print(barNimi+" loses "+hploss+" hitpoints!")
            input (barNimi+" howls in pain!")
            input(barNimi+" has "+barHp+" hitpoints left!")
            rotHp=lyönti(rotHp)
        else:
            print (rotNimi+" strikes the "+barNimi+" succesfully!")
            isku=rotBd-(barArmor-rotPiercing)
            barHp-=isku
            isku=str(isku)
            print (rotNimi+" does "+isku+" damage!")
            input (barNimi+" howls in pain!")
            rotHp=lyönti(rotHp)

    print(rotNimi+" has died!")


taistelu(barHp,rotHp)

exit()
