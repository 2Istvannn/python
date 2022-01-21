print("Kérek egy számot: ")
number: int = int

osszeg: int = 0

while(osszeg < 100):
    number = int(input("Kérek még egy számot: "))
    osszeg = osszeg + number
   
    print(f"{osszeg}")