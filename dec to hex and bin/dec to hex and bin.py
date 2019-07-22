unitone,unittwo,unitthree,unitfour,unitfive = '','','','',''

def check(x):
    if x > 9:
        if x == 10:
            return("A")
        if x == 11:
            return("B")
        if x == 12:
            return("C")
        if x == 13:
            return("D")
        if x == 14:
            return("E")
        if x == 15:
            return("F")
    else:
        return(x)


def dec_to_bin(x):
        return int(bin(x)[2:])
    
while True:
    user = int(input("\nenter denary number"))
    bina = dec_to_bin(user)
    if user > 1048576:
        print("must be lower than 1048576")
    else:
        if user > 65536:
            unitone = user // 65536
            x = 65536 * unitone
            user = user - x
            unitone = check(unitone)
        if user > 4096:
            unittwo = user // 4098
            x = 4098 * unittwo
            user = user - x
            untittwo = check(unittwo)
        if user > 256:
            unitthree = user // 256
            x = 256 * unitthree
            user = user - x
            unitthree = check(unitthree)
        if user > 16:
            unitfour = user // 16
            x = 16 * unitfour
            user = user - x
            unitfour = check(unitfour)
        if user > 0:
            unitfive = user
            unitfive = check(unitfive)

        print("In hex this is:",str(unitone)+str(unittwo)+str(unitthree)+str(unitfour)+str(unitfive))
        print("In binary this is: ",bina)




