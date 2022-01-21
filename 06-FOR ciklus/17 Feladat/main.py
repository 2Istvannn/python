atlag: float = 0
szamokOsszege: int = 0
darabSzam: int = 0

print("Kezdő Érték: ")
kezdoErtek: int = int(input())

print("Vég Érték: ")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1,  1):
    szamokOsszege += i
    darabSzam += 1

atlag: float =  szamokOsszege / darabSzam

print(f"{atlag}")