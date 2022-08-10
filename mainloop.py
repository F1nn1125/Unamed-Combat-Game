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
print("Allocate {} skill points to your attributes in order: ".format(skillpoints))
while True:
    try:
        charhp = int(input("- HP = {}".format(charhp)))
        break
    except:
        print("enter a number")
while True:
    try:
        charstam = int(input("- Stamina = {}".format(charstam)))
        break
    except:
        print("enter a number")
while True:
    try:
        charmana = int(input("- Mana = {}".format(charmana)))
        break
    except:
        print("enter a  number")
while True:
    try:
        charstr = int(input("- Strength = {}".format(charstr)))
        break
    except:
        print("enter a number")
while True:
    try:
        characc = int(input("- Accuracy = {}".format(characc)))
        break
    except:
        print("enter a number")
while True:
    try:
        charagil = int(input("- Agility = {}".format(charagil)))
        break
    except:
        print("enter a number")


skillattribution = list(input)

def enemyrand():
    enemy = ri()
    enhp = ri((1.0, 10.0) * level)
    endmg = ri
    enacc = ri
    
startgame.startgame()
