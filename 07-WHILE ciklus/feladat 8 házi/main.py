import os
import time

valasztek: int = 0
uditok: str = ""

while(valasztek == 0):
    uditok = input("Kérem válasszon egy üdítőt!\nFanta: 1\nCola: 2\nEnergia ital: 3\nPepsi: 4\nAz üdítő száma: ")
    if(uditok.isnumeric()):
        valasztek = int(uditok)
        
    else:
        print("Nem számot adott meg!")
        time.sleep(3)
        os.system("cls")

if(valasztek == 1):
    print("Fanta")
elif(valasztek == 2):
    print("Cola")   
elif(valasztek == 3):
    print("Energia ital")
elif(valasztek == 4):
    print("Pepsi")
else:
    print("Ön nem jó számot adott meg!")
    time.sleep(3)
    os.system("cls")