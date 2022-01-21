sum: int = 0

szorzat: int = 1

print("Kezdő érték: ")
kezdoErtek: int = int(input())

print("Vég érték: ")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek +1, 1):
    sum += i
    szorzat *= i
    
print(f"összeg = {sum}")
print(f"szorzat = {szorzat}")

