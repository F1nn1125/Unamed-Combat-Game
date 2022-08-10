from random import randint as ri
import itemvariables as iv
import startgame

level = 1

#Character maker
charrace = input("")
charclass = input("")
skillpoints = 15
charhp = 5
charstam = 5
charmana = 5
charstr = 5
characc = 5
charagil = 5

#Skillpoint allocation
print("Allocate {} skill points to your attributes of Health, Stamina, Mana, Strength, Accuracy and Agility: ".format(skillpoints))
while True:
    try:
        skilladd = int(input("- HP = {}".format(charhp)))
        if skilladd < 0:
            print("enter a number above 0")
            continue
        if skilladd > skillpoints:
            print("You cannot allocate this many!")
            continue
        else:
            charhp = charhp + skilladd
            skillpoints = skillpoints - skilladd
            break
    except:
        print("enter a number")
while True:
    try:
        skilladd = int(input("- Stamina = {} (You have {} skill points left)".format(charstam, skillpoints)))
        if skilladd < 0:
            print("enter a number above 0")
            skilladd = 0
            continue
        if skillpoints < 0:
            print("You cannot allocate this many!")
            skillpoints = skillpoints - skilladd
            skilladd = 0
            continue
        else:
            charstam = charstam + skilladd
        break
    except:
        print("enter a number")
while True:
    try:
        skilladd = int(input("- Mana = {} (You have {} skill points left)".format(charmana, skillpoints)))
        if skilladd < 0:
            print("enter a number above 0")
            skilladd = 0
            continue
        if skillpoints < 0:
            print("You cannot allocate this many!")
            skillpoints = skilladd
            skilladd = 0
            continue
        else:
            charmana = charmana + skilladd
        break
    except:
        print("enter a number")
while True:
    try:
        skilladd = int(input("- Strength = {} (You have {} skill points left)".format(charstr, skillpoints)))
        if skilladd < 0:
            print("enter a number above 0")
            skilladd = 0
            continue
        if skillpoints < 0:
            print("You cannot allocate this many!")
            skillpoints = skilladd
            skilladd = 0
            continue
        else:
            charstr = charstr + skilladd
        break
    except:
        print("enter a number")
while True:
    try:
        skilladd = int(input("- Accuracy = {} (You have {} skill points left)".format(characc, skillpoints)))
        if skilladd < 0:
            print("enter a number above 0")
            skilladd = 0
            continue
        if skillpoints < 0:
            print("You cannot allocate this many!")
            skillpoints = skilladd
            skilladd = 0
            continue
        else:
            characc = characc + skilladd
        break
    except:
        print("enter a number")
while True:
    try:
        skilladd = int(input("- Agility = {} (You have {} skill points left)".format(charagil, skillpoints)))
        if skilladd < 0:
            print("enter a number above 0")
            skilladd = 0
            continue
        if skillpoints < 0:
            print("You cannot allocate this many!")
            skillpoints = skilladd
            skilladd = 0
            continue
        else:
            charagil = charagil + skilladd
        break
    except:
        print("enter a number")
    
print(charhp)
print(charstam)
print(charmana)
print(charstr)
print(characc)
print(charagil)

def enemyrand():
    enemy = ri()
    enhp = ri((1.0, 10.0) * level)
    endmg = ri
    enacc = ri
    
startgame.startgame()
