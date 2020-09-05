####################################
#              @Lucas06c           #
####################################
# License: GPL v3
# enemy_main.py


# Main enemy code. Work In Progres. 

import json  # Nedeed to acces data.
import sys
sys.path.append("./scripts")    # Idk but this works for me.
from panic.panic import Panic
from colored import fore, back, style, fg, bg, attr   # That module works for the formatting and coroling of the output text.

panic = Panic

class Enemy:     # Create class enemy
 
    def __init__(self, enemy_id): # Idk what this do, but else this doesent work.
        self.enemy_id = enemy_id


    
    def enemy_get_info(self): # Acces to a JSON file wich contains the stats of enemys.
        try:    # If the program can't find the path to the JSON file should display an error msg.
            with open("D:\Dead-is-in-the-deepts\scripts\enemy\enemys.json") as json_enemys: # Opens the JSON file whit all the info
                data = json.load(json_enemys)
        except(OSError): # The error msg.
            panic.panic(" Fatal error trying to open the enemys.json file, look in GitHub issues for the correct fix. \n Oopss... Follow the link below and there you will find the correct fix. \n Issue link: https://github.com/Lucas06c/Dead-is-in-the-deepts/issues/2")

        # Gets all the data from the JSON file. 

        enemy_name = data["monster"][self.enemy_id]["name"]     
        enemy_hp = data["monster"][self.enemy_id]["hp"]
        enemy_dmg = data["monster"][self.enemy_id]["dmg"]
        
        enemy_stats = {"name" : enemy_name, "hp" : enemy_hp, "dmg" : enemy_dmg}     # Get the enemy stats from the json.

        return enemy_stats  # Return the enemy stats.
        


    def enemy_display_info(self): # Gives info about the enemy and stats.
        enemy_stats = Enemy.enemy_get_info(self)
        enemy_name = enemy_stats.get("name")
        enemy_hp = enemy_stats.get("hp")
        enemy_dmg = enemy_stats.get("dmg")    

        bestiary_color = fg("#7c5706")  # Those vars are for coloring the "Bestiary" in the info menu.
        hp_color = fg("#21c912")        # That color is for the hp number in the enemy_display_info() menu.
        dmg_color = fg("#db1e0d")       # Color var for the dmg number in the menu. 
        res = attr("reset")             # That var is for resetting the style and color after every formatting. 

        # Prints out a menu with info about the enemy. Like hp and that stuff. 
        print("\n" + "-" * 30 + style.BOLD +" Enemy Info " + style.RESET + "-" + 38)
        print("|    +" + style.BOLD + " Name  -> " + style.RESET + style.DIM + enemy_name + style.RESET) # Name of the enemy.
        print("|    +" + style.BOLD + " Hp    -> " + style.RESET + hp_color + str(enemy_hp) + res)   # Hp  The str() is for convert int values to str because the hp and the dmg are int values.
        print("|    +" + style.BOLD + " Dmg   -> " + style.RESET + dmg_color + str(enemy_dmg) + res)# Dmg
        print("|                                                                               ")
        print("|   " + style.BOLD + " \->" + style.RESET + " This monster already have an entry in the " + bestiary_color + "Bestiary." + res)
        print("-" * 80)     # Updated this for cleaner code.

    def enemy_appears(self): 





