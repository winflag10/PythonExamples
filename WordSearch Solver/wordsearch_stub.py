# Word search Program
# John_Watkins
# Sept 2018


def get_name():  # Purpose :- Returns your Student Number and Name in the format - ID|Fname_Sname
    return "187438|John_Watkins"


def print_puzzle(puzzle):   # Purpose :- Print out the puzzle in a nice format with a space between each letter
    for row in puzzle:
        print(row.replace("", " "))
    print("\n")


def load_words_to_find(f_name):  # Open the file and read the words to find in from there
    word_list = []
    f = open(f_name, "r")
    data = " "
    while data != "":
        data = f.readline()
        word_list.append(data.replace(" ", "").replace("\n", "").upper())
    word_list.remove("")
    #word_list = sorted(word_list,reverse=True)#  Sorts the words into order so that words that appear inside of other words are found after the longer words
    return word_list





def find_horizontal(puzzle, words, replace_with, found):  # Find all words which are horizontally in place (left to right and right to left), return the puzzle and list of found words
    module_output = []
    for line in puzzle:
        module_output.append(line)
    for found_word in found:
        try:
            words.remove(found_word)
        except:
            pass
    print("TEST HORIZ")
    for i in range(len(module_output)):
        print(i)
        row = module_output[i]
        print(row)
        print(words)
        for word in words:
            if word in row:
                print("FOUND :-",word)
                found.append(word)
                module_output[i] = module_output[i].replace(word,replace_with*len(word))
            if word[::-1] in row:
                found.append(word)
                module_output[i] = module_output[i].replace(word[::-1],replace_with*len(word))
    
    print(module_output)
    print("END TEST")
    return module_output, found







def rotate_puzzle(puzzle):  # Rotate the puzzle so up-down becomes left-right
    #currently only works if the puzzle grid is square
    rotatePuz = [""]*len(puzzle[0])
    for row in puzzle:
        index = len(puzzle[0])-1
        for char in row:
            rotatePuz[index] = rotatePuz[index] + char
            index -= 1    
    return rotatePuz


def find_vertical(puzzle, words, found):  # Find all words which are up-down by rotating the puzzle then back
    module_output, found = find_horizontal(puzzle, words, "|" , found)
    for i in range(3):
       module_output = rotate_puzzle(module_output)
    return module_output,found


    
def find_diagonal(puzzle, words, found):
    for found_word in found:
        try:
            words.remove(found_word)
        except:
            pass
    height = len(puzzle)  #y
    width = len(puzzle[0])  #x
    for word in words:
        for x in range(width):
            for y in range(height):
                start = puzzle[x][y]
                if word[0] == start:
                    UR, UL, DR, DL = start, start, start, start
                    for i in range(len(word)-1):                       
                        try:
                            UR = UR + puzzle[x+(i+1)][y-(i+1)]
                            UL = UL + puzzle[x-(i+1)][y-(i+1)]
                            DR = DR + puzzle[x+(i+1)][y+(i+1)]
                            DL = DL + puzzle[x-(i+1)][y+(i+1)]
                        except IndexError:
                            pass
                    if word == UR:
                        puzzle = replace_diagonal(puzzle,word,x,y,"UR")
                        found.append(word)
                    if word == UL:
                        puzzle = replace_diagonal(puzzle,word,x,y,"UL")
                        found.append(word)
                    if word == DR:
                        puzzle = replace_diagonal(puzzle,word,x,y,"DR")
                        found.append(word)
                    if word == DL:
                        puzzle = replace_diagonal(puzzle,word,x,y,"DL")
                        found.append(word)
                    #print("UR ",UR," UL ",UL," DR ",DR," DL ",DL)

    for word in words:
        word = word[::-1]
    for word in words:
        for x in range(width):
            for y in range(height):
                start = puzzle[x][y]
                if word[0] == start:
                    UR, UL, DR, DL = start, start, start, start
                    for i in range(len(word)-1):                       
                        try:
                            UR = UR + puzzle[x+(i+1)][y-(i+1)]
                            UL = UL + puzzle[x-(i+1)][y-(i+1)]
                            DR = DR + puzzle[x+(i+1)][y+(i+1)]
                            DL = DL + puzzle[x-(i+1)][y+(i+1)]
                        except IndexError:
                            pass
                    if word == UR:
                        puzzle = replace_diagonal(puzzle,word,x,y,"UR")
                        found.append(word)
                    if word == UL:
                        puzzle = replace_diagonal(puzzle,word,x,y,"UL")
                        found.append(word)
                    if word == DR:
                        puzzle = replace_diagonal(puzzle,word,x,y,"DR")
                        found.append(word)
                    if word == DL:
                        puzzle = replace_diagonal(puzzle,word,x,y,"DL")
                        found.append(word)
                    #print("UR ",UR," UL ",UL," DR ",DR," DL ",DL)
                    
                        
                    
    return puzzle,found


def replace_diagonal(puzzle, word, x , y, direction):  # Replace the found diagonal word with a symbol
    module_output = []
    for line in puzzle:
        module_output.append(line)
    module_output[x] = list(module_output[x])
    module_output[x][y] = "\\"
    module_output[x] = "".join(module_output[x])
    for i in range(len(word)-1):
        if direction == "UR":
            row = list(module_output[x+(i+1)])
            row[y-(i+1)] = "\\"
            module_output[x+(i+1)] = "".join(row)
        if direction == "UL":
            row = list(module_output[x-(i+1)])
            row[y-(i+1)] = "\\"
            module_output[x-(i+1)] = "".join(row)
        if direction == "DR":
            row = list(module_output[x+(i+1)])
            row[y+(i+1)] = "\\"
            module_output[x+(i+1)] = "".join(row)
        if direction == "DL":
            row = list(module_output[x-(i+1)])
            row[y+(i+1)] = "\\"
            module_output[x-(i+1)] = "".join(row)
    
    return module_output


def show_only_words(original, puzzle):
    for x in range(len(puzzle[0])):
        for y in range(len(puzzle)):
            if puzzle[x][y] != "." and puzzle[x][y] != "\\" and puzzle[x][y] != "|":
                row = list(original[x])
                row[y] = "*"
                original[x] = "".join(row)
   
    return original


def Missing_Words(words, found):
    missing = []
    for word in words:
        if word not in found:
            missing.append(word)
    return missing


def search_for_words(puzzle, words):
    found = []
    p1, found = find_horizontal(puzzle, words, ".", found)
    p2 = rotate_puzzle(p1)
    p3, found = find_vertical(p2, words, found)
    p4, found = find_diagonal(p3, words, found)
    missing = Missing_Words(words, found)
    return p4, missing

if __name__ == '__main__':
    import copy
    puzzle = ["FUNCTIONRRIRAIXXX",
              "RAIOONFRCCPWONXXX",
              "PTCSNOBEUITOLOXXX",
              "BNCACIANTOSLIHXXX",
              "RBYOLILYNREFBTXXX",
              "HYYNOGESTIBRIYXXX",
              "AATTSIONCMCENPXXX",
              "UORTENRRCBFVAUXXX",
              "CEBEECVWIERORIXXX",
              "PROCESSORTOPYFXXX",
              "OHCOMPUTERHSOSXXX",
              "YCYPRESREOSMRWXXX",
              "OATHBRMVTHHCTRXXX",
              "PGORWOOUlPBITEXXX",
              "XXXXXXXlXXXXXXXXX",
              "XXXXXXeXXXXXXXXXX",
              "XXXXXhXXXXXXXXXXX",]
    original_puzzle = copy.deepcopy(puzzle)
    print_puzzle(puzzle)
    words = load_words_to_find("words.txt")
    answer,missing = search_for_words(puzzle,words)
    only_words = show_only_words(original_puzzle,answer)
    print_puzzle(answer)
    print_puzzle(only_words)
    print("Missing Words:",missing)
