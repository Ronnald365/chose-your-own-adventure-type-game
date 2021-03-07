# still in development
import random
import time
a=random.randrange(1,1000000000000)
while True:
    time.sleep(1)
    r = input("do you want to play a game? y/n: ")
    if r == 'y':
            time.sleep(1)
            print("ok lets get started")
            time.sleep(6)
            break
    if r == 'n':
        time.sleep(1)
        print("ok maybe next time")
        time.sleep(1)
        print("resetting game...")
        time.sleep(6)
time.sleep(1)
print("welcome player #"+str(a))
time.sleep(1)
print("press 'a' to see the instructions")
r = input()
if r == 'a':
    time.sleep(1)
    print("you need to chose the right answers to proceed and your objective is to get back to your living room good luck and don't die press ENTER to start the game")
    r = input()
    if r == "ENTER":
        time.sleep(1)
        print("starting the game")
    while True:
        print("before you can start answer this question. What is sheldon coppers joke word? if you do not know just write skip")
        password = input("what is the word?: ")
        if password == "bazinga":
            time.sleep(6)
            print("correct")
            break
        elif password =='skip':
            time.sleep(1)
            print("you skipped the question")
            break
        else:
            time.sleep(6)
            print("denied:'(")
    time.sleep(1)
    print("type based adventure game")
    while True:
        print("you see a huge bear in front of a bridge you want to pass what do you do? hi or boo or sneak or wait? type one")
        r = input()
        if r == 'hi':
            time.sleep(1)
            print("the bear accepts your kindness and lets you pass")
            break
        elif r=='sneak':
            time.sleep(1)
            print("you try to sneak past the bear but step on a twig the bear awakes and you are dead :'(")
        elif r=='wait':
            time.sleep(1)
            print("you wait but realize it is winter and the bear would not wake up so it is pointless and you leave :'(")
        elif r=='boo':
            time.sleep(1)
            print("the bear gets scared and you are ded:'(")
        else:
            time.sleep(1)
            print("error")
    while True:
        time.sleep(1)
        print("you stand before four paths type west or east or north west or north east?")
        r = input()
        if r == 'west':
            time.sleep(1)
            print("you walk west and survive")
            break
        elif r == 'east':
            time.sleep(1)
            print("you east path and die:'(")
        elif r=='north west':
            time.sleep(1)
            print("you go north west and die :'(")
        elif r=='north east':
            time.sleep(1)
            print("you go north east and die :'(")
    while True:
        time.sleep(1)
        print("you stand before four doors type 1 or 2 or 3 or 4")
        r = input()
        if r == '1':
            time.sleep(1)
            print("you take the first door and get killed by a spider :'(")
        elif r == '2':
            time.sleep(1)
            print("you take the second door and land in you living room")
            time.sleep(1)
            print("you win :)")
            break
            time.sleep(1)
            print("congratulations plz check out my git hub I also have many other programms on repl.it")
        elif r=='3':
            time.sleep(1)
            print("you take the third door and die :'(")
        elif r=='4':
            time.sleep(1)
            print("you thake the fourth door and die :'(")
            time.sleep(1)
            print("well done player #"+str(a))
            #this will be on git hub
