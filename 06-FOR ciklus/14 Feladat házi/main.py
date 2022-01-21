hettelOszthatoSzamok: int = 0
ottelOszthatoSzamok: int = 0

print("Kezdő érték: ")
kezdoErtek: int = int(input())

print("Vég érték: ")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1, 1):
    if (i % 5 == 0 and i % 7 == 0):
        ottelOszthatoSzamok += 1
        hettelOszthatoSzamok += 1
    elif(i % 5 == 0):
        ottelOszthatoSzamok += 1
    elif (i % 7 == 0):
        hettelOszthatoSzamok += 1

if (hettelOszthatoSzamok > ottelOszthatoSzamok):
    print("A héttel osztható számok a nagyobbak")
elif (hettelOszthatoSzamok < ottelOszthatoSzamok):
    print("Az öttel osztható számok a nagyobbak")
else:
    print("Egyenlőek")