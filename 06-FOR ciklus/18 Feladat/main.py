elojelValto: int = 1
osszeg: int = 0

print("Kezdő érték: ")
kezdoErtek: int = int(input())

print("Vég érték: ")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1, 1):
    osszeg = osszeg +- i * elojelValto
    elojelValto = elojelValto * (-1)

print(f"{osszeg}")