import random, time, os

WIN_COMBINATIONS = [(6, 7, 8),(3, 4, 5),(0, 1, 2),(6, 3, 0),(7, 4, 1),(8, 5, 2),(6, 4, 2),(8, 4, 0),]
board = ["-","-","-","-","-","-","-","-","-"]
save = []
    

def draw():
    global board
    print("\nBOARD LAYOUT")
    line()
    print("|7|8|9|")
    line()
    print("|4|5|6|")
    line()
    print("|1|2|3|")
    line()
    print("\nCURRENT BOARD")
    line()
    print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|")
    line()
    print("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")
    line()
    print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    line()

def line():
    print("-------")


def check_won(add_me):
    global board, save
    for a,b,c in WIN_COMBINATIONS:
        if ((board[a] == board[b] == board[c])and(board[a] in "xo")):
            draw()
            print("\nplayer "+board[a]+" wins!!")
            data = board[a] + "win"
            if add_me:
                save.append(data)
            return True
    return False

def check_full():
    global board
    count = 0
    for item in board:
        if item in "xo":
            count+=1
    if count == 9:
        return True
    else:
        return False

def clear_page():
    os.system('cls')
    
def init_pvp():
    global save, board
    turn = "x"
    while (check_won(True) == False and check_full() == False):
        draw()
        print("player "+ turn +"'s turn")
        while True:
            user = int(input("Where would you like to place your token?"))
            try:
                if board[user-1] == "-":
                    board[user-1] = turn
                    move = turn + ";" + str(user)
                    save.append(move)
                    print(save)
                    break
                else:
                    print("There is already a token in this space try again\n")
            except:
                print("Invalid location number try again\n")
        clear_page()
        if turn == "x":
            turn = "o"
        else:
            turn = "x"
    if check_full() == True and not check_won(False):
        draw()
        print("The game was a draw")
        save.append("draw")
    save = format_save(save)
    #f = open("tictactoedatabase/pvp.txt","a+")
    #f.write(save)
    #f.close()


def init_generate(): #I Understand this is redundant but it allowed me to test
   global save, board #for the expected ai that i wanted to implement
   turn = "x"
   while (check_won(True) == False and check_full() == False):
       time.sleep(0.1)
       draw()
       print("player "+ turn +"'s turn")
       while True:
           user = random.randrange(9)+1
           try:
               if board[user-1] == "-":
                   board[user-1] = turn
                   move = turn + str(user)
                   save.append(move)
                   print(save)
                   break
               else:
                   print("There is already a token in this space try again\n")
           except:
               print("Invalid location number try again\n")
       clear_page()
       if turn == "x":
           turn = "o"
       else:
           turn = "x"
   if check_full() == True and not check_won(False):
       draw()
       print("The game was a draw")
       save.append("draw")
   save = format_save(save)
   f = open("tictactoe database/pvp.txt","a+")
   f.write(save)
   f.close()




def format_save(save):
    length = len(save)
    new_save = ""
    for i in range(length-1):
        new_save = new_save + save[i]
        new_save = new_save + ","
    new_save = new_save + save[length-1] + "\n"
    return new_save
        

for i in range(50):
    init_pvp()
    save = []
    board = ["-","-","-","-","-","-","-","-","-"]
#for i in range(10):
    #init_generate()
#input("press enter to quit")

