from random import randint as ri
import itemvariables as iv
import startgame

level = 1

#Character maker
charrace = input("""
Choose a race:
1. Orc
2. Elf
3. Human
""")
charclass = input("""
1. Fighter (mele damage scaling)
2. Mage (mana & magic damage scaling)
3. Brute (hitpoint scaling)
""")
skillpoints = 15
charhp = 5
charstam = 5
charmana = 5
charstr = 5
characc = 5
charagil = 5

#Skillpoint allocation
def skillpointallocation():
    print("Allocate {} skill points to your attributes of Health, Stamina, Mana, Strength, Accuracy and Agility: ".format(skillpoints))
    while True:
        try:
            skilladd = int(input("- Health = {} (You have {} skill points left.): ".format(charhp, skillpoints)))
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
            skilladd = int(input("- Stamina = {} (You have {} skill points left.): ".format(charstam, skillpoints)))
            if skilladd < 0:
                print("enter a number above 0")
                continue
            if skilladd > skillpoints:
                print("You cannot allocate this many!")
                continue
            else:
                charstam = charstam + skilladd
                skillpoints = skillpoints - skilladd
                break
        except:
            print("enter a number")
    while True:
        try:
            skilladd = int(input("- Mana = {} (You have {} skill points left.): ".format(charmana, skillpoints)))
            if skilladd < 0:
                print("enter a number above 0")
                continue
            if skilladd > skillpoints:
                print("You cannot allocate this many!")
                continue
            else:
                charmana = charmana + skilladd
                skillpoints = skillpoints - skilladd
                break
        except:
            print("enter a number")
    while True:
        try:
            skilladd = int(input("- Strength = {} (You have {} skill points left.): ".format(charstr, skillpoints)))
            if skilladd < 0:
                print("enter a number above 0")
                continue
            if skilladd > skillpoints:
                print("You cannot allocate this many!")
                continue
            else:
                charstr = charstr + skilladd
                skillpoints = skillpoints - skilladd
                break
        except:
            print("enter a number")
    while True:
        try:
            skilladd = int(input("- Accuracy = {} (You have {} skill points left.): ".format(characc, skillpoints)))
            if skilladd < 0:
                print("enter a number above 0")
                continue
            if skilladd > skillpoints:
                print("You cannot allocate this many!")
                continue
            else:
                characc = characc + skilladd
                skillpoints = skillpoints - skilladd
                break
        except:
            print("enter a number")
    while True:
        try:
            skilladd = int(input("- Agility = {} (You have {} skill points left.): ".format(charagil, skillpoints)))
            if skilladd < 0:
                print("enter a number above 0")
                continue
            if skilladd > skillpoints:
                print("You cannot allocate this many!")
                continue
            else:
                charagil = charagil + skilladd
                skillpoints = skillpoints - skilladd
                break
        except:
            print("enter a number")

# Enemy random gen
def enemyrand():
    enemy = ri()
    enhp = ri((1, 10) * level)
    endmg = ri((1, 5) * level)
    enacc = ri(40,80)
    
startgame.startgame()
