print("x = ")
x: int = int(input())

print("y = ")
y: int = int(input())

print("z = ")
z: int = int(input())

if (x % y == 0 and x % z == 0):
    print(f"{x} osztható {y} és {z}")
elif (x % y == 0):
    print(f"{x} osztható {y}")
elif (x % z == 0):
    print(f"{x} osztható {z}")
else:
    print(f"{x} nem osztható {z} és {y}")