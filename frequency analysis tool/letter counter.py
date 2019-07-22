letters = {}
text = input("Input text\n>").lower().replace(" ","").replace("\n","")
for letter in text:
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1
highest = ("",0)
for item in letters:
    print(item,str(letters[item]))
    if highest[1] < letters[item]:
        highest = (item,letters[item])
print("Highest: "+str(highest[0])+"~"+str(highest[1]))
input()
