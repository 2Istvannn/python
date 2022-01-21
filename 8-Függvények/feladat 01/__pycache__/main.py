from matematikafuggvenyek import *
from inputLIB import *

osszeg: float = None
kulonbseg: float = None
szorzat: float = None
hanyados: float = None

x: float = None
y: float = None

x = tizedesSzamBeolvasasa("Kérem az x értékét: ")
y = tizedesSzamBeolvasasa("kérem az y értékét: ")

osszeg = osszeadas(x, y)
kulonbseg = kivonas(x, y)
szorzat = szorzas(x, y)
hanyados = osztas(x, y)

print(f"A számok összege: {osszeg}")
print(f"A számok különbsége: {kulonbseg}")
print(f"A számok szorzata: {szorzat}")
print(f"A számok hányadosa: {hanyados}")
