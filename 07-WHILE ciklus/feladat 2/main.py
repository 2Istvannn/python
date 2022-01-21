#I. név nem lehet üres string
#II. szóközök (1 vagy több)
#III. név hossza (minimum 3 karakter)

import os
import time

nev: str = ""

while(nev == "" or nev.isspace() or len(nev) < 3 ):
    nev = str(input("Kérem adja meg a nevét: "))
    if(nev == ""):
        print("Nem írt be semmit!")
        time.sleep(3)
        os.system("cls")
    elif(nev.isspace ()):
        print("Nem lehet szóközt írni!")
        time.sleep(3)
        os.system("cls")
    elif(len(nev) < 3):
        print("Nem lehet kevesebb mint 3 tag!")
        time.sleep(3)
        os.system("cls")
    else:
        print(f"Üdvözlöm {nev}!")
        break