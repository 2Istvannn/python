paratlanSzamokOsszege: int = 0
parosSzamokOsszege: int = 0
atlag: float = 0


print("Kezdő érték: ")
kezdoErtek: int = int(input())

print("Vég érték: ")
vegErtek: int = int(input())

for i in range (kezdoErtek, vegErtek + 1, 1):
    if (i % 2 == 0):
        parosSzamokOsszege += i
    else:
        paratlanSzamokOsszege += i

    atlag: float = (paratlanSzamokOsszege + parosSzamokOsszege) / 2

print(f"{atlag}")