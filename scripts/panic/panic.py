####################################
#              @Lucas06c           #
####################################
# License: GPL v3

# File that means to error handling while program running, insted of only crashing.

from colored import fore, back, style, fg, bg, attr     # Module requerid for formatting correctly the error msg.


class Panic:     # Creates a class for the error handeling. 
            
    def panic(error):   
        error_color = fg("#ff0303")     # 255 red color for the "FATAL ERROR"
        warn_color = fg("#ff8002")      # orange like color for the error msg.
        res = attr("reset")


        # Prints out the error msg. 
        print(" ")
        print("     " + style.BOLD + error_color + "[X] FATAL ERROR!" + res)
        print(" ________________________________________________________________________")
        if error == "":
            print(warn_color + "  No error msg especified.  \n  Something just go wrong." + res)
        else:
            print( warn_color + error + res)
        print(" ")
        print(" ")
        input(" Hit intro to exit...")
        exit()



