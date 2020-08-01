####################################
#              @Lucas06c           #
####################################
# License: GPL v3
# Edited: 2020/08/01


# Main enemy code. Work In Progres. 

from colored import fore, back, style, fg, bg, attr   # That module works for the formatting and coroling of the output text.


class Enemy:     # Create class enemy
 
    def __init__(self, name, hp, dmg): # Idk what this do, but else this doesent work.
        self.name = name
        self.hp = hp 
        self.dmg = dmg
        self.attacks = attacks

    def enemy_info(self): # Gives info about the enemy and stats. 

        bestiary_color = fg("#7c5706")  # Those vars are for coloring the "Besniary" 
        res = attr("reset")             # in the info menu.

        print("")
        print("------------------------------" + style.BOLD +" Enemy Info " + style.RESET + "------------------------------")
        print("|    +" + style.BOLD + " Name  -> " + style.RESET + style.DIM + self.name + style.RESET) # Name of the enemy.
        print("|    +" + style.BOLD + " Hp    -> " + style.RESET + str(self.hp))   # Hp  The str() is for convert int values to str because the hp and the dmg are int values.
        print("|    +" + style.BOLD + " Dmg   -> " + style.RESET + str(self.dmg))# Dmg
        print("|                                                                               ")
        print("|   " + style.BOLD + " \->" + style.RESET + " This monster already have an entry in the " + bestiary_color + "Bestiary." + res)
        print("--------------------------------------------------------------------------------")


""" 
    def enemy_combat(self):
        
        kind_of_attacks = {
            "simp_punch" : 2
        }
    
        def attack():
            kind_of_attacks.get(attacks, "ERROR: Read the log and report") 
"""      



Slime = Enemy("Slime", 5, 2, "simp_punch")

Slime.enemy_info()