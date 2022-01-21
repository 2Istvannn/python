#pip3 install keyboard
#csomagok importálása
import os
#import keyboard
import time

#változók definiálása

#a szám amit be kell olvasni
    #kezdőértéke a None, mivel a while ciklusban ki tudom ezt használni az ismétlések vizsgálatára
    #vagyis a ciklus mindaddig futtatjuk, míg a number változónak nem lesz szám értéke
number: int = None 
    #segéd változó a beolvasott értéket fogja tárolni
data: str = ""

#while ciklus, ami mindaddig fog futni míg a number változó nem kap szám értéket
#azaz az értéke nem None lesz
while(number == None):
    #beolvasás a konzolról és a beolvasptt értéket eltároljuk a data változóba
    data = input("Kérem a számot: ")
    #megvizsgáljuk, hogy a beolvasott érték (string) számra alakítható e
    #mindegy, hogy ez a szám int vagy float típusú
    #isdigit() -> bool változót ad vissza
    if(data.isdigit()):
        #ha az isdigit() függvény értéke igaz, akkor számot írt be a felhasználó
        #amit mi BIZTOS át tudunk szám típussá alakítani
        number = int(data)
    #az isdigit() függvény értéke hamis, azaz a felhasználó nem számot írt be
    #így a number változó értéke továbbra is None marad, azaz a felhasználó nem számot írt be
    #a ciklus ismételni kell
    else:
        print("\nNem számot adott meg!")
        #a programot futtató szálat (therd) elaltatjuk 3 másodpercre
        time.sleep(3)
        #letöröljük a képernyőt
        os.system("cls")

        #print("\nA folytatáshoz nyomjon meg az ENTER billentyűt.")
        #egy végtelen WHILE ciklust írunk, mivel arra fogunk várni, hogy a felhasználó 
        #lenyomja a kért billentyűzetet (ENTER)
        #while (True):
        #    figyeljük, hogy a felhasználó lenyomta e az ENTER gombot
        #    if (keyboard.is_pressed('enter')):
        #        letöröljük a képernyőt
        #        os.system("cls")
        #        kilépünk a belső (végtelen) while ciklusból
        #        break
#kiírjuk a beolvasott számot
print(f"A beolvasott szam {number}")