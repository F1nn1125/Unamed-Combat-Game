from random import randint as ri
import itemvariables as iv
import startgame

# Preset Variables
level = 1
skillpoints = 15

# Allocated skill points
charhp = 5
charstam = 5
charmana = 5
charstr = 5
characc = 5
charagil = 5

# Recalculated stats

recalc_mana = charmana * (level + 1)
recalc_hp = charhp * (level + 1)
recalc_stam = charstam * (level +1)
recalc_str = charstr * (level + 1)
recalc_acc = characc * (level +1)
recalc_agil = charagil * (level + 1)

# Character maker
while True:
    while True:
        try:
            charrace = int(input("""
Choose a race:

1. Orc (health & damage scaling)
2. Elf (mana & agility scaling)
3. Human (accuracy & stamina scaling)

"""))
            break
        except:
            print("enter 1, 2 or 3")
    while True:
        try:
            charclass = int(input("""
Choose a class:

1. Fighter (mele damage scaling)
2. Mage (mana scaling)
3. Brute (hitpoint scaling)

"""))
            break
        except:
            print("enter 1, 2 or 3")

            # Ignore my stupid code here i know theres a better way to do this
    if charrace <= 0 or charrace > 3:
        print(" enter either 1, 2 or 3")
        continue
    elif charclass <= 0 or charclass > 3:
        print("enter either 1, 2 or 3")
        continue

    #More stupid code please ignore
    elif charrace == 1 and charclass == 1:
        recalc_hp = charhp * (level + 5)
        recalc_str = charstr * (level + 10)
        break
    elif charrace == 1 and charclass == 2:
        recalc_hp = charhp * (level + 5)
        recalc_str = charstr * (level + 5)
        recalc_mana = charmana * (level + 5)
        break
    elif charrace == 1 and charclass == 3:
        recalc_hp = charhp * (level + 10)
        recalc_str = charstr * (level + 5)
        break
    elif charrace == 2 and charclass == 1:
        recalc_str = charstr * (level + 5)
        recalc_mana = charmana * (level + 5)
        recalc_agil = charagil * (level + 5)
        break
    elif charrace == 2 and charclass == 2:
        recalc_mana = charmana * (level + 10)
        recalc_agil = charagil * (level + 5)
        break
    elif charrace == 2 and charclass == 3:
        recalc_mana = charmana * (level + 5)
        recalc_agil = charagil * (level + 5)
        recalc_hp = charhp * (level + 5)
        break
    elif charrace == 3 and charclass == 1:
        recalc_acc = characc * (level + 5)
        recalc_stam = charstam * (level + 5)
        recalc_str = charstr * (level + 5)
        break
    elif charrace == 3 and charclass == 2:
        recalc_acc = characc * (level + 5)
        recalc_stam = charstam * (level + 5)
        recalc_mana = charmana * (level + 5)
        break
    elif charrace == 3 and charclass == 3:
        recalc_acc = characc * (level + 5)
        recalc_stam = charstam * (level + 5)
        recalc_hp = charhp * (level + 5)
        break
    # The shitty code is over (not really)

#Skillpoint allocation
def skillpointallocation(charhp, charmana, charstr, charstam, characc, charagil, skillpoints):
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
skillpointallocation(charhp, charmana, charstr, charstam, characc, charagil, skillpoints)
print(charclass, charrace)