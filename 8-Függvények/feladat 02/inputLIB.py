import time
import os

def tizedesSzamBeolvasasa(szoveg: str) -> float:
    szam: float = None

    while(szam == None):
        data: str = input(szoveg)
        if(data.replace("-", "").replace(".", "").isdigit()):
            szam = float(data)
            return szam
        else:
            print("Nem számot adott meg")
            time.sleep(3)
            os.system("cls")

def egeszSzamBeolvasasa(szoveg: str) -> int:
    szam: int = None

    while(szam == None):
        data: str = input(szoveg)
        if(data.replace("-", "").isdigit()):
            szam = int(data)
            return szam
        else:
            print("Nem számot adott meg")
            time.sleep(3)
            os.system("cls")

def nevBekeres() -> str:
    nev: str = None

    while(nev == None):
        data: str = input("Kérem a nevét: ")
        #milyen hosszú a név
        if(len(data) < 3):
            print("Túl rövid a név, min. 3 karakter")
            time.sleep(3)
            os.system("cls")
        else:
            nev = data
            
    return nev