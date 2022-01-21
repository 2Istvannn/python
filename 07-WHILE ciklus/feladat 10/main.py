import os
import time

n: int = None
data: str = ""
parosSzamok: int = 0
ottelOszthatoSzamok: int = 0
tizenEgyelOszthatoSzamokSzama: int = 0
hettelOszthatoHaromMaradek: int = 0

while(n == None or n < 0 or n > 100):
    data = input("Kérek egy legalább maximum kétjegyű számot: ")
    if(data.isnumeric()):
        n = int(data)
    else:
        print("Nem számot adott meg!")
        time.sleep(3)
        os.system("cls")

for i in range(0, n + 1,  1):
    if(i % 2 == 0):
        parosSzamok += i
        print(f"A páros számok: {i}")
    
for i in range(0, n + 1, 1):
    if(i % 5 == 0):
        ottelOszthatoSzamok += i
        
print(f"Az öttel osztható számok összege: {ottelOszthatoSzamok}")

for i in range(0, n + 1, 1):
    if(i % 11 == 0):
        tizenEgyelOszthatoSzamokSzama += 1

print(f"A 11-el osztható számok száma: {tizenEgyelOszthatoSzamokSzama}")

for i in range(0, n + 1, 1):
    if(i % 7 == 3):
        hettelOszthatoHaromMaradek += 1
print(f"Azok a számok amelyek héttel oszthatóak és 3-mat adnak maradékul: {hettelOszthatoHaromMaradek}")