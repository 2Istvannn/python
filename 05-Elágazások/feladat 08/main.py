print("x = ")
x: int = int(input())

if (x % 4 == 0 and x % 6 == 0):
    print(f"{x} osztható 4-el és 6-al")
else:
    print(f"{x} nem osztható 4-el és 6-al")