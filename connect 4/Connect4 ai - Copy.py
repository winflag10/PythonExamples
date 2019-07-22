##################################--main code--####################################
import random,copy,json
size = 7
turn = 1 #1=X 2=O

def turn_increment():
    global turn
    turn += 1
    if turn > 2:
        turn = 1


def print_grid(grid):
    print("\n")
    for i in range(len(grid[0])):
        print(i+1,end="")
        print(" ",end="")
    print("\n")
    for row in grid:
        print(" ".join(row))

        
def create_grid(size):
    grid = [['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-']]
    return grid

def check_won_full(grid):
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
    grid = create_grid(size)
    print("Welcome to connect 4!")
    while True:
        user = input("Enter 1 to play against a friend\nEnter 2 to play against a computer\n>")
        if user == "1":
            init_("pvp",grid)
            break
        elif user == "2":
            init_("pve",grid)
            break
        elif user == "3":
            grid_copy = grid
            generate_tree(grid_copy)
        else:
            print("that is an invalid input")


        
def init_(mode,grid):
    print_grid(grid)
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
            if place(column,"X",grid):
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
                if place(column,"O",grid):
                   print("place succsessful")
                   print_grid(grid)
                   break
                else:
                   print("This column is either full or doesn't exist.")
        elif mode == "pve":
            while True:
                column = random.randrange(size)+1
                if place(column,"O",grid):
                   print("Computer has played")
                   print_grid(grid)
                   break
                else:
                   pass


    turn_increment()
    if check_won_full(grid)[0]:
        print_grid(grid)
        if check_won_full(grid)[1] == 1:
            print("\nX wins!!")
        elif check_won_full(grid)[1] == 2:
            print("\nO wins!!")
        else:
            print("\nThe game ended in a draw.")
    else:   
        init_(mode,grid)


def place(column,symbol,grid):
    if column > len(grid[0]) or grid[::-1][len(grid)-1][column-1] != "-":
        return (False,grid)
    index = column - 1
    placed = False
    for i in range(len(grid[0])):
        row = grid[::-1][i]
        if not placed:
            if row[index] == "-":
                row[index] = symbol
                grid[::-1][i] = row
                placed = True
    return (True,grid)
##################################--main code--####################################


###################################--ai code--#####################################

def generate_tree(grid):
    #gen L1
    tree = generate_next_layer(grid,1,"O")                    

    #gen L2
    for L1 in tree:                                           
        new_item = generate_next_layer(tree[L1],2,"X")
        tree[L1] = new_item

    #gen L3
    for L1 in tree:                                           
        for L2 in tree[L1]:
            new_item = generate_next_layer(tree[L1][L2],3,"O")
            tree[L1][L2] = new_item
    
    #gen L4
    for L1 in tree:                                           
        for L2 in tree[L1]:
            for L3 in tree[L1][L2]:
                new_item = generate_next_layer(tree[L1][L2][L3],4,"X")
                tree[L1][L2][L3] = new_item

    
    #print out all possible board states 4 moves on... warning laggy..
    print(json.dumps(tree, indent=4, sort_keys=True))
    print("done")




def generate_next_layer(grid,LayerNo,piece):#takes in a grid and returns a dict with all 
    global size
    Layer = {}
    for move in range(size):
        grid_copy = copy.deepcopy(grid)
        key_name = "L"+str(LayerNo)+"M"+str(move+1)
        Layer[key_name] = place(move+1,piece,grid_copy)[1]
    return Layer





def board_heuristic(board):
    score = 0
    #checks for win and loss +- 40000 in either case ignore draw as this will 
    if check_won_full(grid)[0]:
        if check_won_full(grid)[1] == 1:
            score -= 40000
        elif check_won_full(grid)[1] == 2:
            score += 40000

    #check for block opponent
    
    

###################################--ai code--#####################################



main_and_select_mode(size)






































