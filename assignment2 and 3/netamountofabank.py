trans = input("Enter the transaction: ")

amount = 0
newnum = ""
char = ""

for i in trans:
    if i.isalpha():
        char = i
    elif i == " ":
        if newnum:
            if char == "D":
                amount += int(newnum)
            elif char == "W":
                amount -= int(newnum)
            newnum = ""
    elif i.isdigit():
        newnum += i

if newnum:
    if char == "D":
        amount += int(newnum)
    elif char == "W":
        amount -= int(newnum)

print("Amount:", amount)