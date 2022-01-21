print("x = ")
x: int = int(input())

print("y = ")
y: int = int(input())

if (x < y):
    print(f" {x}, {y}")
elif (y < x):
    print(f" {y}, {x}")
else:
    print(f" {x}, {y}")