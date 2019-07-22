import random
size = 7
grid = []
turn = 1 #1=X 2=O

def turn_increment():
    global turn
    turn += 1
    if turn > 2:
        turn = 1


def print_grid():
    global grid
    print("\n")
    for i in range(len(grid[0])):
        print(i+1,end="")
        print(" ",end="")
    print("\n")
    for row in grid:
        print(" ".join(row))

        
def create_grid(size):
    global grid
    grid = [['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-']]
    

def check_won_full():
    global grid
    global size
    for symbol in "XO":
        for c in range(size-3):
            for r in range(size):
                if grid[r][c] == symbol and grid[r][c+1] == symbol and grid[r][c+2] == symbol and grid[r][c+3] == symbol:
                    if symbol == "X":
                        return(True,1)
                    else:
                        return(True,2)
        for c in range(size):
            for r in range(size-3):
                if grid[r][c] == symbol and grid[r+1][c] == symbol and grid[r+2][c] == symbol and grid[r+3][c] == symbol:
                    if symbol == "X":
                        return(True,1)
                    else:
                        return(True,2)
        for c in range(size-3):
            for r in range(size-3):
                if grid[r][c] == symbol and grid[r+1][c+1] == symbol and grid[r+2][c+2] == symbol and grid[r+3][c+3] == symbol:
                    if symbol == "X":
                        return(True,1)
                    else:
                        return(True,2)
        for c in range(size-3):
            for r in range(3, size):
                if grid[r][c] == symbol and grid[r-1][c+1] == symbol and grid[r-2][c+2] == symbol and grid[r-3][c+3] == symbol:
                    if symbol == "X":
                        return(True,1)
                    else:
                        return(True,2)
    count = 0
    for row in grid:
        for item in row:
            if item == "-":
                count +=1
    if count == 0:
        return(True,0)
    else:
        return(False,0)
    #will return a tuple with True/False for whether the game is over and 1 or 2 as to the player who won or a 0 if draw.


def main_and_select_mode(size):
    global grid
    create_grid(size)
    print("Welcome to connect 4!")
    while True:
        user = input("Enter 1 to play against a friend\nEnter 2 to play against a computer\n>")
        if user == "1":
            init_("pvp")
            break
        elif user == "2":
            init_("pve")
            break
        else:
            print("that is an invalid input")


            
#####THIS COULD BE REWRITTEN MORE EFFICIENTLY#######
def init_(mode):
    print_grid()
    global grid
    global size
    global turn
    if turn == 1:
        print("It is player 1's turn(X)")
        
        while True:
            while True:
                try:
                    column = int(input("please select the column you would like to place in\n>"))
                    break
                except:
                    print("You must enter an integer")
            if place(column,"X"):
               print("place succsessful")
               break
            else:
               print("This column is either full or doesn't exist.")
    elif turn == 2:
        if mode == "pvp":
            print("It is player 2's turn(O)")
            while True:
                while True:
                    try:
                        column = int(input("please select the column you would like to place in\n>"))
                        break
                    except:
                        print("You must enter an integer")
                if place(column,"O"):
                   print("place succsessful")
                   print_grid()
                   break
                else:
                   print("This column is either full or doesn't exist.")
        elif mode == "pve":
            while True:
                column = random.randrange(size)+1
                if place(column,"O"):
                   print("Computer has played")
                   print_grid()
                   break
                else:
                   pass


    turn_increment()
    if check_won_full()[0]:
        print_grid()
        if check_won_full()[1] == 1:
            print("\nX wins!!")
        elif check_won_full()[1] == 2:
            print("\nO wins!!")
        else:
            print("\nThe game ended in a draw.")
    else:   
        init_(mode)

#####THIS COULD BE REWRITTEN MORE EFFICIENTLY#######



def place(column,symbol):
    global grid
    if column > len(grid[0]) or grid[::-1][len(grid)-1][column-1] != "-":
        return False
    index = column - 1
    placed = False
    for i in range(len(grid[0])):
        row = grid[::-1][i]
        if not placed:
            if row[index] == "-":
                row[index] = symbol
                placed = True
    return True




main_and_select_mode(size)




