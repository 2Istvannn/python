import os
import time


osszeg: int = 0
number: int = int
number = int(input("Kérek egy számot: "))

while(osszeg < 100):
    
    if(number < 100 and number > 0):
            osszeg = osszeg + number
            print(f"{osszeg}")
            number = int(input("Kérek egy újabb számot: "))
    
    elif(osszeg > 100):
        print("Az összeg nem lehet több mint 100")
        time.sleep(3)
        os.system("cls")
        break

    else:
        number == None
        print("\nCsak számot lehet írni!")
        time.sleep(3)
        os.system("cls")
        break

print(f"{osszeg}")
