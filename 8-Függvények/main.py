import time
import os
#hibaüzenet
def hiba(uzenet: str) -> None:
    print(uzenet)
    time.sleep(3)
    os.system("cls")


#pontszám bekérése
def pontBekeres() -> int:
    pontSzam: int = None
    data: str = None
    while(pontSzam == None):
        data: str = input("Kérem adja meg a pontszámot: ")
        if(data.isdigit()):
            pontSzam=int(data)
            if(pontSzam >= 0 and pontSzam <= 100):
                return pontSzam
            else:
                pontSzam = None
                hiba("0 és 100 között adjon meg számot!")
                
        else:
            hiba("Csak számot adhat meg!")
           

#pontszám vizsgálata
def vizsgalat(szam: int) -> int:
    if(szam < 50):
        return 1
    elif(szam >= 50 and szam < 60):
        return 2
    elif(szam >= 60 and szam < 70):
        return 3
    elif(szam >= 70 and szam < 85):
        return 4
    else:
        return 5


#kiírás
def kiiratas(pontSzam: int, erdemjegy: int) -> None:
    print(f"Önnek ennyi pontszáma lett: {pontSzam}, ezt az osztályzatot kapja: {erdemjegy}!")


#főprogram
pontSzam: int = pontBekeres()
erdemjegy: int = vizsgalat(pontSzam)
kiiratas(pontSzam, erdemjegy)

