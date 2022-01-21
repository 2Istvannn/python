print("x = ")
x: int = int(input())

print("y = ")
y: int = int(input())

print("z = ")
z: int = int(input())

if (x < y and x < z and y < z):
    print(f"{x} {y} {z}")
elif (x < y and x < z and z < y):
    print(f"{x} {z} {y}")
elif (y < z and y < x and z < x):
    print(f"{y} {z} {x}")
elif (y < z and y < x and x < z):
    print(f"{y} {x} {z}")
elif (z < x and z < y and x < y):
    print(f"{z} {x} {y}")
elif (z < x and z < y and y < x):
    print(f"{z} {y} {x}")
elif (x == y and x == z):
    print(f"{x} {y} {z}")
elif (x == y and x < z):
    print(f"{x} {y} {z}")
elif (x == y and x > z):
    print(f"{z} {x} {y}")
elif (x == z and x < y):
    print(f"{x} {z} {y}")
elif (x == z and x > y):
    print(f"{y} {x} {z}")
elif (z == y and y < x):
    print(f"{y} {z} {x}")
elif (z == y and x < z):
    print(f"{x} {z} {y}")
else:
    print(f"{x} {y} {z}")