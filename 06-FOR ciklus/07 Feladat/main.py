print("Kezdő érték: ")
kezdoErtek: int = int(input())

print("Vég érték: ")
vegErtek: int = int(input())

for i in range(vegErtek, kezdoErtek, -1):
    print(i)