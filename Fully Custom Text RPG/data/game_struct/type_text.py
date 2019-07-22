import time, sys
def type(text):
    for i in text:
        delay = 0.05
        time.sleep(delay)
        print(i,end="")
        sys.stdout.flush()
    print()

type("aysdvajbfdhjasbfhjsbaUHJFDBHKJAA")
