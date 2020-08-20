####################################
#              @Lucas06c           #
####################################
# License: GPL v3
# Test script 

# Test scrip, only for testing propouses.

import json 

try:                                                                # If colored is not installed should return that isn't installed.
    from colored import fore, back, style, fg, bg, attr
except(ModuleNotFoundError):
    print(" [X] -> FATAL ERROR IMPORTING PACAKGE's")
    print("  \  -> run: pip install colored")
    input(" Hit intro to exit...")
    exit()


# The program requires that to import some package

import sys              
sys.path.append("./scripts")

try:
    from enemy.enemy_main import *                          # Importing enemy package.
    from panic.panic import *                               # Import panic package.
        
except(ModuleNotFoundError):
    error_color = fg("#ff0303")     # 255 red color.
    warn_color = fg("#ff8002")      # orange like.
    green_color = fg("#40d317")     # green. 
    res = attr("reset")             # Reseting the color and style.

    print(style.BOLD + error_color + " [X]" + res + style.BOLD + "  -> FATAL ERROR IMPORTING PACKAGE's")
    input("    \->" + res + style.DIM + " Hit intro to exit...")
    exit()
  

def test(): # The main function of this engine.

    # Loads a json file to grab data from it. In that case, the program took the version and the current state of the program and things like that.
    try:    # If the program can't find the path to the JSON file should display an error msg.
        with open("D:/Dead-in-the-Deepts/test/test.json") as json_test_info: # Opens the JSON file whit all the info about the engine.
            data = json.load(json_test_info)
    except(OSError): # The error msg.
        panic.panic(" Fatal error trying to open the test.json file, look in GitHub issues for the correct fix. \n Oopss... Follow the link below and there you will find the correct fix. \n Issue link: https://github.com/Lucas06c/Dead-is-in-the-deepts/issues/2")

    version = data.get("version")           # Grabs the version from the json file.
    current_state = data.get("state")       # Grabs the state of development fro the code.


    error_color = fg("#ff0303")     # 255 red color.
    warn_color = fg("#ff8002")      # orange like.
    green_color = fg("#40d317")     # green. 
    res = attr("reset")             # Reseting the color and style.
    print(style.BOLD + warn_color + " [!]  ->" + res + style.BOLD +" Starting DitD test engine..." + res)
    print(style.DIM + "   \-> version [" + style.BOLD + version + res + "] | current state == [ " + style.BOLD + current_state + res + " ]")
    print(style.BOLD + green_color + " [ok] ->" + res + style.BOLD + " Imported succesfully the needed packages. \n")
    print(style.BOLD + warn_color + " [!]" + res + style.BOLD + "  -> Proced to check if packages are okey?")

    try:
        imp = input(style.DIM + "   \-> [" + style.BOLD + green_color + "Yes" + res + "/" + style.BOLD + error_color + "No" + res + "]")
    except(KeyboardInterrupt):
        panic.panic("KeyboardInterrup error. Restart the program and NOT clik again a random ctrl C...")
    
    # Create an empty variable for it use in next's lines...
    imp_result = ""

    if imp != "Y" or "y" or "Yes" or "yes"or "N"or "n"or "No"or "no":
        panic.panic(" Incorrect input... Re run the test and check your grammar... ")
    elif imp == "Y" or "y" or "Yes" or "yes":
        imp_result 

        # THIS IS FUCKING SPAGUETI 
        # FUCK ITALIA, I'M GOING TO WORK WITH ENEMYS


    


test()






