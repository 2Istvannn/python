import os
import time

penz: float = None
honapokSzama: int = 0
data: str = ""

while(penz == None or penz > 50000 or penz < 10000):
    data = input("Kérek egy számot 10000 és 50000 között!\n")
    if(data.isdigit()):
        penz = int(data)
    else:
        print("Nem számot adott meg!")
        time.sleep(3)
        os.system("cls")

while(penz <= 100000):
    penz = penz * 1.02
    honapokSzama += 1

print(f"{honapokSzama} hónap alatt érte el a 10000Ft-ot 2%-os kamattal")