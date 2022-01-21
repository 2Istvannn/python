print("x = ")
x: int = int(input())

if ( x >= 0 and x <= 9 ):
    print("A szám egyjegyű")
elif ( x >= 10 and x <= 99):
    print("A szám kétjegyű")
elif ( x >= 100 and x <= 999):
    print("A szám háromjegyű")
else:
    print("A szám 4 vagy többjegyű, vagy mínusz előjelű")