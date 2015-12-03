# -*- coding: utf-8 -*-

#kun kirjoittaa talk niin ilmestyy tämä viesti
def talk(npc):

    if npc.ID==5:

        print("You approach the troll, try to establishe contact with him. HE raises his head, tears filling his eyes.")
        print("'"'What do YOU want,'"' the troll asks bluntly, ripe with disinterest.")
        print()
        print("1. Ask what's troubleing the troll.")
        print()
        print("2. Leave him alone.")
        answer = 0
        while answer not in (1,2):
            try:
                answer=int(input("What to do? "))
            except ValueError as e:
                print(e)

        if answer==1:
            print("The troll seems suprised at your question. He hesitates for a while, and says:")
            print("'"'Bah, you would not understand anyway. What do you know about REAL heartache?'"'")
            print()
            print("1. Share a sentiment from your own troubled relationship history. Try to explain")
            print("that even tough you tought that your world ends because of these problems, it")
            print("didn't, and life goes on. Give examples of newfound happines that has crossed your path.")
            print()
            print("2. Tell him to get a grip and recite rowdy lyrics you  heard from the bard a few weeks before,")
            print("glorifying the finer points of being a male specimen with functioning reproductive organs and")
            print("little care for any meaningfull relationships.")

            answer = 0

            while answer not in (1,2):
                try:
                    answer=int(input("What to do? "))
                except ValueError as e:
                    print(e)


            if answer==1:
                print("At firs, the troll seems to not listen. But as something you tell him seems to catch his ear")
                print("as familliar, he get's involved. And before long, you have his full attention. You discuss")
                print("your experiences and their familiarities and you help the troll see a bit further into his own")
                print("future. '"'Gee, i guess im taking it a bit too hard. Heck, i thinkg im doing more harm to myself'"'")
                print("like this than the actual problems i had! I'm out of here, man. Im gonna get a hold of Steve,")
                print("i havent seen him in ages!''")
                print()
                print("The troll stands up and stretches, visibly revitalized. He shouts out to you as he starts jogging")
                print("""towards the entrance to the cave: "Thanks dude! Hope you dont die down here! Good luck with" """)
                print(""" the quest and such!" """)
                print()
                print("The door is now free of any troll-obtrusions.")
                print("PRESS ENTER TO CONTINUE")
                input()
                quest=1
                return quest

            elif answer==2:
                print("The troll just starts crying harder. You clearly don't make a good impression, and the troll")
                print("assumes a fetal position and starts singing some melancholy-ridden troll song.")
                print("PRESS ENTER TO CONTINUE")
                input()
                quest=2
                return quest

        elif answer==2:
            print("You leave him alone")
            quest = 0
            return quest

#Room 13 scene

    if npc.ID==7:
    
        print("Do you wish to intervene?")
        print()
        print("Y/N")
    
        choice=input()

        while answer not in (y,n,Y,N):
                try:
                    answer=int(input("What to do? "))
                except ValueError as e:
                    print(e)
        if choice=="y" or choice=="Y":
            print("Right as the rat is going for the goblins juggular, you kick the foul beast in the ribs, sending it ")
            print("flying accross the room accompanied with a high-pitched squeal. The goblin runs for cover and the rat ")
            print("scatters to it's feet. The bloodthirsty beast comes at you with full force!")
    
            combat(npc)
    
            if npc.hp<=0:
                print("""As the dust settles , the goblin comes up to you. "I can't thank you enough for what you did there!" """)
                print(""" "I'm a janitor here at Zhaltrauc's Lair and i'm usually accompanied by a guard in this vermin """)
                print(""" infested first level. But today they made me go alone, with horrible consequenses. I know you aren't""")
                print(""" supposed to be here, but after what you did, i don't care. I was a goner for sure and the orcs are""")
                print("""to blame for neglecting me. Here, take this deck full of aces. It's what i usually use to get back at""")
                print("""the orc's. I clean the table in the card game's they have at the second level's exit. Come to think""")
                print("""of it, that might be the reason they left me to my own advices today..." """)
                print()
                print("""You get the Deck o' Ace's""")
        elif choice=="n" or choice=="N":
            print("You carefully skip around the gurgling goblin as the rat tears at it's throat. You clearly are of low ")
            print("empathy and even though you pretend to not care, the hopeless and fear-ridden screams of a dying humanoid")
            print("will haunt you for the rest of your life.")

#room 17 scene

    if npc.ID==8:
        print("Do you wish to free the slave?")
        print()
        print("Y/N")
        choice8=input()
        while answer not in (y,n,Y,N):
                try:
                    answer=int(input("What to do? "))
                except ValueError as e:
                    print(e)

        if choice8=="y" or choice8=="Y":
            print("You Attack the orc's! Battle commences!")

            combat()

            if npc.hp<=0:
                print("""The prisoner approaches you, relief visible in her face. "I tought i'd never see another day , thank""")
                print("""you stranger. Like you, i was on my way to destroy Zhaltrauc. I just couldn't stand watching the """)
                print("""realm suffer as he started to grow in power. But apparently i was not as prepared as i tougth. I do,""")
                print("""however, have a valuable piece of information. Zhaltrauc himself is an old evil spirit of aking """)
                print("""thrown down from his throne by the people he reigned over. He assumed the form of a lich king and""")
                print("""stole the sacred Light Stone from my father's, the king of my land, castle. It's what he uses to """)
                print("""channel the evil powers and wouldn't have lasted this long without it. The stone is used for good """)
                print("""but in the wrong hands... but i digress. Beware of the stone! He keeps it on his crown and will""")
                print("""youse it against you! You will go blind and be unable to fight. You need to find a way to fight""")
                print("""the blinding light that the magical gem emanates. I wish for you to exceed. Farewell!" The """)
                print("""adventuring maiden gives you a health potion. She then takes a sword from the orc guards and makes""")
                print("""her way back to the first level. """)

        elif choice8=="n" or choice8=="N":
            print("You hide behind a pillar and observe as the prisoner is dragged away.")
            print("You can only guess what will come of her.")


    else:
        print("Converstion with that {} is not written yet.".format(npc.NPCName))
        return 0
