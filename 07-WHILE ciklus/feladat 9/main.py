import os 
import time

szam: int = None
data: str = ""

while(szam == None or szam < 100 or szam > 999):
    data = input("Kérek egy számot amit 3 jegyű és osztható 7-tel!\n")
    if(data.isnumeric()):
        szam = int(data)
    else:
        print("Nem számot adott meg!")
        time.sleep(3)
        os.system("cls")

if(szam % 7 == 0):
    print(f"Jó szám adott meg")
else:
    print("A szám nem osztható 7-tel!")
    time.sleep(3)
    os.system("cls")