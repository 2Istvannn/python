parosSzamokOsszege: int = 0
paratlanSzamokOsszege: int = 0

print("Kezdő érték: ")
kezdoErtek: int = int(input())

print("Vég érték: ")
vegErtek: int = int(input())

for i in range (kezdoErtek, vegErtek + 1, 1):
    if (i % 2 == 0):
        parosSzamokOsszege += i
    else:
        paratlanSzamokOsszege += i
    
if (parosSzamokOsszege > paratlanSzamokOsszege):
    print("A páros számok összege a nagyobb")
elif (paratlanSzamokOsszege > parosSzamokOsszege):
    print("A páratlan számok összege a nagyobb")
else:
    print("Egyenlőek")
