####################################
#              @Lucas06c           #
####################################
# License: GPL v3

# File that means to error handling while program running, insted of only crashing.

from colored import fore, back, style, fg, bg, attr     # Module requerid for formatting correctly the error msg.


class Panic:
            
    def panic(error):
        error_color = fg("#ff0303")
        warn_color = fg("#ff8002") 
        res = attr("reset")

        print(" ")
        print("     " + style.BOLD + error_color + "[X] FATAL ERROR!" + res)
        print(" ________________________________________________________________________")
        print( warn_color + error + res)
        print(" ")
        print(" ")
        input(" Hit intro to exit...")
        exit()



