a, b = 0, 1
def fib (n):
    a, b = 0, 1
    while a < n:
        print(a)
        a,b=b,a+b

x = int(input("how high do you want the fibbonachi sequence to?"))
fib(x)


input()
