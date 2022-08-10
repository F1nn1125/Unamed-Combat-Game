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
charhp = int(input("- HP = {}".format(charhp)))
print("- Stamina = {}".format(charstam))
print("- Mana = {}".format(charmana))
print("- Strength = {}".format(charstr))
print("- Accuracy = {}".format(characc))
print("- Agility = {}".format(charagil))


skillattribution = list(input)

def enemyrand():
    enemy = ri()
    enhp = ri((1.0, 10.0) * level)
    endmg = ri
    enacc = ri
    
startgame.startgame()
