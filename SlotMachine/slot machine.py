#FRUIT MACHINE 
#Write a program to simulate a Fruit Machine that displays three symbols at
#random from Cherry, Bell, Lemon, Orange, Star, Skull. 
#The player starts with £1 credit, with each go costing 20p.
#If the Fruit Machine “rolls” two of the same symbol, the user wins 50p.
#The player wins £1 for three of the same and £5 for 3 Bells.
#The player loses £1 if two skulls are rolled and all of his/her money
#if three skulls are rolled. The player can choose to quit with the winnings
#after each roll or keep playing until there is no money left. “

#importing modules for program expansion
#waiting for spin
#closing windows
#pygame-graphics-not installed yet

import time,random,sys

end_of_game = False

bal_pence = 500

#defining variables and weighted choices

weighted_options = [("bell",2),("cherry",2),("lemon",2),("orange",2),("star",2),("skull",2)]
reel = [val for val, cnt in weighted_options for i in range(cnt)]
roll_result = []

#start of spin

def spin(bal_pence):
    if bal_pence < 20:
        print("sorry you can't afford to spin")
        return False
    else:
        bal_pence -= 20


        for x in range (3):
            roll_result.append(random.choice(reel))
        #will send to a display function later
        print (roll_result)
        #check function selects new balance
        bal_pence += check(roll_result,bal_pence)
        return bal_pence

#end of spin

#start of bal check
    
def bal_check(bal_pence,end_of_game):
    if end_of_game:
        prefix = "You walk away with "
        print(prefix+"£"+"{:.2f}".format(bal_pence/100))
    elif bal_pence < 0:
        print("You walk away with nothing")
    else:
        prefix = "You have "
        suffix = ''
        print(prefix+"£"+"{:.2f}".format(bal_pence/100))

#end of bal check

#start of check

def check(roll_result,bal_pence):
    winnings = 0
    if roll_result[0] == roll_result[1]:
        if roll_result[0] == roll_result[2]:
            if roll_result[0] == "bell":
                #3 bells
                print("You won £5")
                return 500
            elif roll_result[0] == "skull":
                #3 skulls
                print("Unlucky you lost all your money!!")
                return(bal_pence - bal_pence - bal_pence)
                
            else:
                #3 of anything else
                print("You won £1")
                return 100
                
        else:
            if roll_result[0] == "skull":
                #2 skulls
                print("Unlucky you lost £1")
                return -100
            else:
                #2 of anything else
                print("You won 50p")
                return 50
    elif roll_result[1] == roll_result[2] or roll_result[0] == roll_result[2]:
        if roll_result[2] == "skull":
            #2 skulls
            print("Unlucky you lost £1")
            return -100
        else:
            #2 of anything else
            print("You won 50p")
            return 50
    else:
        #no pattern
        print("Better luck next time")
        return 0

#end of check

#start of core program
    
print("\nWelcome to the python fruit machine\nYou have £5 to play with\nType bal to see your balance\npress enter to test your luck and spin the wheels\n1 spin costs 20p\nTo walk away with the money youve got type quit")
while not end_of_game:
    choice = input()
    choice=choice.lower()
    if choice == "quit":
        end_of_game = True
        print("Thanks for playing :)")
        bal_check(bal_pence,end_of_game)
    elif choice == "bal":
        bal_check(bal_pence,end_of_game)
    else:
        bal_pence = spin(bal_pence)
        if not bal_pence or bal_pence == 0:
            end_of_game = True
        roll_result = []
        if bal_pence:
            bal_check(bal_pence,end_of_game)



input()


#end of core program






