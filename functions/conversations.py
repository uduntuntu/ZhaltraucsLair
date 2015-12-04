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
    
        answer=input()

        while answer not in ("y","n","Y","N"):
                try:
                    answer=input("What to do? ")
                except ValueError as e:
                    print(e)
        if answer=="y" or answer=="Y":
            print("Right as the rat is going for the goblins juggular, you kick the foul beast in the ribs, sending it ")
            print("flying accross the room accompanied with a high-pitched squeal. The goblin runs for cover and the rat ")
            print("scatters to it's feet. The bloodthirsty beast comes at you with full force!")
    
            return 1
    
        elif answer=="n" or answer=="N":
            print("You carefully skip around the gurgling goblin as the rat tears at it's throat. You clearly are of low ")
            print("empathy and even though you pretend to not care, the hopeless and fear-ridden screams of a dying humanoid")
            print("will haunt you for the rest of your life.")

            return 0

#room 17 scene

    if npc.ID==8:
        print("Do you wish to free the slave?")
        print()
        print("Y/N")
        answer8=input()
        while answer8 not in ("y","n","Y","N"):
                try:
                    answer8=int(input("What to do? "))
                except ValueError as e:
                    print(e)

        if answer8=="y" or answer8=="Y":
            print("You Attack the orcs! Battle commences!")
            return 1



        elif answer8=="n" or answer8=="N":
            print("You hide behind a pillar and observe as the prisoner is dragged away.")
            print("You can only guess what will come of her. You may continue east, west or south")
            quest = 1
            return quest

    else:
        print("Converstion with that {} is not written yet.".format(npc.NPCName))
        return 0

    #room 34

    if npc.ID==19:
    
        a=0
        
        match=False
        
        answerStrings2=["kill","Kill","zhaltrauc","Zhaltrauc","kill zhaltrauc","kill Zhaltrauc","Kill zhaltrauc","Kill Zhaltrauc","Defeat zhaltrauc","Defeat Zhaltrauc","defeat zhaltrauc","Defeat Zhaltrauc"]
        answerStrings3=["african","Aafrican","european","European","african?","Aafrican?","european?","European?"]
        
        while a<3:
        
            print("What is your name?")
            nameAnswer=input()
            if nameAnswer == player.playername:
                a+=1
            else:
                print("You are sent flying, like a leaf in the wind, into the gorge. You have answered wrongly. Oh, and you died.")
                break
            print("What is your quest?")
            questAnswer=input()
            for item in answerStrings2:
                if item in questAnswer:
                    match=True
                if match==True:
                    a+=1
                if a==1:
                    print("You are sent flying, like a leaf in the wind, into the gorge. You have answered wrongly. Oh, and you died.")
                    break
        
        
            print("What is the air-speed velocity of an unladen swallow?")
            swallowAnswer=input()
            for item in answerStrings3:
                if item in swallowAnswer:
                    match=False
                if match==False:
                    a+=1
                    if a>=3:
                        print(""""What?  I don't know that!  Auuuuuuuugh!" the bridge keeper screams as he flies into the gorge""")
                        print("and dies. You are free to traverse the bridge and enter the doorway south.")
                        break
                else:
                        print("You are sent flying, like a leaf in the wind, into the gorge. You have answered wrongly. Oh, and you died.")
                        break
        
        
