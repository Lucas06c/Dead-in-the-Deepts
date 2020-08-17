####################################
#              @Lucas06c           #
####################################
# License: GPL v3
# Edited: 2020/08/03


# Main enemy code. Work In Progres. 

import json  # Nedeed to acces data.
from panic.panic import Panic
from colored import fore, back, style, fg, bg, attr   # That module works for the formatting and coroling of the output text.

panic = Panic

class Enemy:     # Create class enemy
 
    def __init__(self, enemy_id): # Idk what this do, but else this doesent work.
        self.enemy_id = enemy_id


    
    def enemy_get_info(self): # Acces to a JSON file wich contains the stats of enemys.
        try:
            with open("D:\Dead-is-in-the-deepts\scripts\enemys.json") as json_enemys: # Opens the JSON file whit all the info
                data = json.load(json_enemys)
        except(OSError):
            panic.panic(" Fatal error trying to open the enemys.json file, look in GitHub issues for the correct fix. \n Oopss... Follow the link below and there you will find the correct fix. \n Issue link: https://github.com/Lucas06c/Dead-is-in-the-deepts/issues/2")


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

        bestiary_color = fg("#7c5706")  # Those vars are for coloring the "Bestiary" in the info menu.
        hp_color = fg("#21c912")        # That color is for the hp number in the enemy_display_info() menu.
        dmg_color = fg("#db1e0d")       # Color var for the dmg number in the menu. 
        res = attr("reset")             # That var is for resetting the style and color after every formatting. 

        print("")
        print("------------------------------" + style.BOLD +" Enemy Info " + style.RESET + "--------------------------------------")
        print("|    +" + style.BOLD + " Name  -> " + style.RESET + style.DIM + enemy_name + style.RESET) # Name of the enemy.
        print("|    +" + style.BOLD + " Hp    -> " + style.RESET + hp_color + str(enemy_hp) + res)   # Hp  The str() is for convert int values to str because the hp and the dmg are int values.
        print("|    +" + style.BOLD + " Dmg   -> " + style.RESET + dmg_color + str(enemy_dmg) + res)# Dmg
        print("|                                                                               ")
        print("|   " + style.BOLD + " \->" + style.RESET + " This monster already have an entry in the " + bestiary_color + "Bestiary." + res)
        print("--------------------------------------------------------------------------------")




# Test function, only for testing and development process, not expected to be on unestable. 
def test():     
    Spider = Enemy("spider")
    Spider.enemy_display_info()
    Slime = Enemy("slime")
    Slime.enemy_display_info()
    Undedad_One = Enemy("undead_one")
    Undedad_One.enemy_display_info()

test()