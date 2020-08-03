####################################
#              @Lucas06c           #
####################################
# License: GPL v3
# Edited: 2020/08/03


# Main enemy code. Work In Progres. 
import json  # Nedeed to acces data.
from colored import fore, back, style, fg, bg, attr   # That module works for the formatting and coroling of the output text.


class Enemy:     # Create class enemy
 
    def __init__(self, monster_id): # Idk what this do, but else this doesent work.
        self.monster_id = monster_id


    def enemy_get_info(self): # Acces to a JSON file wich contains the stats of enemys.
        with open("enemys.json") as json_enemys:



    def enemy_display_info(self): # Gives info about the enemy and stats. 
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





Slime = Enemy("slime")

Slime.enemy_info()