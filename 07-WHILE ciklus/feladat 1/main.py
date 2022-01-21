import os
import time

number: int = None
data: str = ""

while (number == None):
    data = input("Kérem a számot: ")
    if(data.isdigit()):
        number = int(data)
        if(number < 9 and number > 0):
            pass
        else:
            number == None
            print("\nNem jó számot adott meg!")
            time.sleep(3)
            os.system("cls")
    else:
        print("\nNem jó számot adott meg!")
        time.sleep(3)
        os.system("cls")

print(f"A beolvasott szám  {number}")