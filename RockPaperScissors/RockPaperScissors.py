
print("Welcome to rock paper scissors!")
#play again option?
#fix with functions
mode = 0
playing = True
import random
userscore = 0
computerscore = 0
rps = ["rock","paper","scissors"]
rpsls = ["rock","paper","scissors","lizard","spock"]
while True:
    try:
        rounds = int(input("How many rounds do you want to play?"))
        break
    except:
        pass
if rounds == 666:
    mode = 1
    rounds = 5
i = 0

weighted_choices = [('rock',1), ('paper', 1), ('scissors', 1)]
a = [val for val, cnt in weighted_choices for i in range(cnt)]
nerdy_weighted_choices = [('rock',1), ('paper', 1), ('scissors', 1), ('lizard', 1), ('spock', 1)]
b = [val for val, cnt in nerdy_weighted_choices for i in range(cnt)]

while i != rounds:
    if mode == 0:
        choice = random.choice(a)
        user = input("\nRock,Paper or Scissors?")
        user = user.lower()
        if user not in rps:
            print("Thats not an option")
        else:
            print("You chose",user)
            print("The computer chose",choice)
            if choice == user:
                print("Draw")
                i+=1
                print("you have played",i,"rounds")
            elif(choice == "paper" and user == "rock" or
                choice == "scissors" and user == "paper" or
                choice == "rock" and user == "scissors"):
                print("you lose")
                computerscore += 1
                print("The computer is on",computerscore)
                print("You are on",userscore)
                i+=1
                print("you have played",i,"rounds")
            else:
                print("you win")
                userscore += 1
                print("The computer is on",computerscore)
                print("You are on",userscore)
                i+=1
                print("you have played",i,"rounds")
    else:
        choice = random.choice(b)
        user = input("\nRock,Paper,scissors,lizard or spock?")
        user = user.lower()
        if user not in rpsls:
            print("Thats not an option")
        else:
            print("You chose",user)
            print("The computer chose",choice)
            if choice == user:
                print("Draw")
                i+=1
                print("you have played",i,"rounds")
            elif (choice == "paper" and (user == "rock" or user == "spock") or
            choice == "rock" and (user == "lizard" or user == "scissors") or
            choice == "scissors" and (user == "paper" or user == "lizard") or
            choice == "lizard" and (user == "spock" or user == "paper") or
            choice == "spock" and (user == "rock" or user == "scissors")):
                print("you lose")
                computerscore += 1
                print("The computer is on",computerscore)
                print("You are on",userscore)
                i+=1
                print("you have played",i,"rounds")
            else:
                print("you win")
                userscore += 1
                print("The computer is on",computerscore)
                print("You are on",userscore)
                i+=1
                print("you have played",i,"rounds")
print("\nThe final scores are..")
print("The computer scored",computerscore)
print("You scored",userscore)
if userscore > computerscore:
    print("You won the game!!!")
elif computerscore > userscore:
    print("You lost better luck next time")
elif computerscore == userscore:
    print("The game was a draw")
else:
    pass
input()


