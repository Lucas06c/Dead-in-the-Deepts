####################################
#              @Lucas06c           #
####################################
# License: GPL v3
# Edited: 2020/08/03


# Main enemy code. Work In Progres. 
import json  # Nedeed to acces data.
from colored import fore, back, style, fg, bg, attr   # That module works for the formatting and coroling of the output text.


class Enemy:     # Create class enemy
 
    def __init__(self, enemy_id): # Idk what this do, but else this doesent work.
        self.enemy_id = enemy_id


    
    def enemy_get_info(self): # Acces to a JSON file wich contains the stats of enemys.
        with open("D:\Dead-is-in-the-deepts\scripts\enemys.json") as json_enemys: # Opens the JSON file whit all the info
            data = json.load(json_enemys)
        
        enemy_name = data["monster"][self.enemy_id]["name"]
        enemy_hp = data["monster"][self.enemy_id]["hp"]
        enemy_dmg = data["monster"][self.enemy_id]["dmg"]
        
        enemy_stats = {"name" : enemy_name, "hp" : enemy_hp, "dmg" : enemy_dmg}

        return enemy_stats
        


        


    def enemy_display_info(self): # Gives info about the enemy and stats.
        enemy_stats = Enemy.enemy_get_info(self)
        enemy_name = enemy_stats.get("name")
        enemy_hp = enemy_stats.get("hp")
        enemy_dmg = enemy_stats.get("dmg")    

        bestiary_color = fg("#7c5706")  # Those vars are for coloring the "Bestiary" 
        res = attr("reset")             # in the info menu.

        print("")
        print("------------------------------" + style.BOLD +" Enemy Info " + style.RESET + "------------------------------")
        print("|    +" + style.BOLD + " Name  -> " + style.RESET + style.DIM + enemy_name + style.RESET) # Name of the enemy.
        print("|    +" + style.BOLD + " Hp    -> " + style.RESET + str(enemy_hp))   # Hp  The str() is for convert int values to str because the hp and the dmg are int values.
        print("|    +" + style.BOLD + " Dmg   -> " + style.RESET + str(enemy_dmg))# Dmg
        print("|                                                                               ")
        print("|   " + style.BOLD + " \->" + style.RESET + " This monster already have an entry in the " + bestiary_color + "Bestiary." + res)
        print("--------------------------------------------------------------------------------")





Slime = Enemy("slime")

Slime.enemy_display_info()