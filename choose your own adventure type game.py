import random
import time
a=random.randrange(1,1000000000000)
while True:
    time.sleep(1)
    r = input("do you want to play a game? y/n: ")
    if r == 'y':
            time.sleep(1)
            print("ok lets get started")
            time.sleep(1)
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
        print("before you can start answer this question. What is sheldon coppers joke word?")
        password = input("what is the word?:")
        #it will work
        if password == "bazinga":
            time.sleep(6)
            print("correct")
        #I believe in me
            break
        else:
            time.sleep(6)
            print("denied:'(")
    time.sleep(1)
    print("type based adventure game")
    while True:
        print("you see a huge bear in front of a bridge you want to pass what do you say? hi or boo? type one")
        r = input()
        if r == 'hi':
            time.sleep(1)
            print("the bear accepts your kindness and lets you pass")
            break
        else:
         if r == 'boo':
            time.sleep(1)
            print("the bear gets scared and you are ded:'(")
    while True:
        time.sleep(1)
        print("you stand before two paths type left or right?")
        r = input()
        if r == 'left':
            time.sleep(1)
            print("you take the left path and survive")
            break
        else:
         if r == 'right':
            time.sleep(1)
            print("you take the right path and die:'(")
    while True:
        time.sleep(1)
        print("you stand before two doors type 1 or 2")
        r = input()
        if r == '1':
            time.sleep(1)
            print("you take the first door and get killed by a spider :'(")
        else:
         if r == '2':
            time.sleep(1)
            print("you take the second door and land in you living room")
            time.sleep(1)
            print("you win :)")
            time.sleep(1)
            print("congratulations plz check out my git hub I also have many other programms on repl.it")
            break
print("well done player #"+str(a))
#this will be on git hub
