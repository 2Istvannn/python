print("x = ")
x: int = int(input())

print("y = ")
y: int = int(input())

if (x > y):
    print(f"{x} nagyobb mint {y}")
elif (y > x):
    print(f"{y} nagyobb mint {x}")
else:
    print(f"{x} egyenlő {y}")