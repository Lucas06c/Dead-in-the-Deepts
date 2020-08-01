#Lucas's Monster by Rick

# Main enemy code. 

from colored import fore, back, style


class Enemy:     # Create class enemy
 
    def __init__(self, name, hp, dmg): # Idk what this do, but else this doesent work.
        self.name = name
        self.hp = hp
        self.dmg = dmg
"""
    def enemy_info(self): # Gives info about the enemy and stats. 
        
        print("")
        print("------------------------------" + style.BOLD +" Enemy Info " + style.RESET + "------------------------------")
        print("|    +" + style.BOLD + " Name  -> " + style.RESET + self.name) # Name of the enemy.
        print("|    +" + style.BOLD + " Hp    -> " + style.RESET + str(self.hp))   # Hp  The str() is for convert int values to str because the hp and the dmg are int values.
        print("|    +" + style.BOLD + " Dmg   -> " + style.RESET + str(self.dmg))# Dmg
        print("------------------------------------------------------------------------ ")

"""
Slime = Enemy("Slime", 5, 2)

#Slime.enemy_info()

class Human:
    def __init__ (self, hpp):
        self.hpp = hpp

    def damaged(self, result):
        self.result = result
        result = int(Slime.dmg)  -  int(self.hpp)
        print(self.result)

hooman = Human(100)
