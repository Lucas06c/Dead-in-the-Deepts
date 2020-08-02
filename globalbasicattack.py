import random

ph = 100

monsters = {
    "Slime" : { "Name" : "Slime", "Dmg" : 2, "HP" : 5},
    "Zombie" : { "Name" : "Zombie", "Dmg" : 5, "HP" : 10},
    "Spider" : { "Name" : "Spider", "Dmg" : 7, "HP" : 12}, 
    "Skeleton" : { "Name" : "Skeleton", "Dmg" : 10, "HP" : 10}
}

def aslime():                                                   #Slime basic attack
    if ph == 0 or ph > 0:
        print("You died! Your hp dropped to zero")
        pass
    else:
        result = ph 
        result -= monsters["Slime"]["Dmg"]
        print(result)

def azombie():                                                      #Zombie basic attack
    if ph == 0 or ph > 0:
        print("You died! Your hp dropped to zero")          
        pass
    else:
        result = ph 
        result -= monsters["Zombie"]["Dmg"]
        print(result)

def aspider():                                                           #Spider basic attack
    if ph == 0 or ph > 0:
        print("You died! Your hp dropped to zero")
        pass
    else:
        result = ph 
        result -= monsters["Spider"]["Dmg"]
        print(result)

def askeleton():                                                   #Skeleton basic attack
    if ph == 0 or ph < 0:
        print("You died! Your hp dropped to zero")
        pass
    else:
        result = ph 
        result -= monsters[""]["Dmg"]
        print(result)



attacks = [ aslime ,azombie , aspider , askeleton ]


