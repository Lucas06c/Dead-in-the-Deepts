from random import random , randint


game = True
battle = True


while game == True:
    while battle == True:
        ph = 100

        monsters = {
            "Slime" : { "Name" : "Slime", "Dmg" : random.randint(0,3), "HP" : 5},           #This creates a range of damage, from 0 (a miss) to a critical hit
            "Zombie" : { "Name" : "Zombie", "Dmg" : random.randint(0,6), "HP" : 10},
            "Spider" : { "Name" : "Spider", "Dmg" : random.randint(0,8), "HP" : 12}, 
            "Skeleton" : { "Name" : "Skeleton", "Dmg" : random.randint(0,12), "HP" : 10}
        }

        def aslime():
            pew = monsters["Slime"]["Dmg"]                                           #Slime basic attack
            if ph == 0 or ph < 0:
                print("You died! Your hp dropped to zero")                  #TODO finish the pew thing and search in google the errors
                pass
            elif pew == 0:
                print("The monster missed the attack! You lost 0 hp")
            else:
                if pew == 3:
                    print ("Critical attack! You lost 3 hp!")
                else:
                    result = ph 
                    result -= pew
                print(result)

        def azombie():
            pew = monsters["Zombie"]["Dmg"]                       #Zombie basic attack
            if ph == 0 or ph > 0:
                print("You died! Your hp dropped to zero")          
                pass
            elif pew == 0:
                print ("The monster missed the attack! You lost 0 hp")
            else:
                if pew == 6:
                    print ("Critical attack! You lost 6 hp!")
                else:
                    result = ph 
                    result -= pew
                    print(result)

        def aspider():
            pew = monsters["Spider"]["Dmg"]                                                        #Spider basic attack
            if ph == 0 or ph > 0:
                print("You died! Your hp dropped to zero")
                pass
            elif pew == 0:
                print ("The monster missed the attack! You lost 0 hp") 
            else:
                if pew == 8:
                    print ("Critical attack! You lost 8 hp!")
                else:
                    result = ph 
                    result -= pew
                    print(result)

        def askeleton():
            pew = monsters["Skeleton"]["Dmg"]                                                   #Skeleton basic attack
            if ph == 0 or ph > 0:
                print("You died! Your hp dropped to zero")
                pass
            elif pew == 0:
                print("The monster missed the attack! You lost 0 hp")
            else:
                if pew == 12:
                    print ("Critical attack! You lost 12 hp!")
                result = ph 
                result -= pew
                print(result)



        attacks = [ aslime ,azombie , aspider , askeleton ]

        aslime()