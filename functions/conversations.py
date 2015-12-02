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
        try:
            while answer not in (1,2):
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
            try:
                while answer not in (1,2):
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

    else:
        print("Converstion with that {} is not written yet.".format(npc.NPCName))
        return 0