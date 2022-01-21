harommalOszthatoSzamokSzama: int = 0

print("Kezdő érték: ")
kezdoErtek: int = int(input())

print("Vég érték: ")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek + 1, 1):
    if (i % 3 == 0):
        harommalOszthatoSzamokSzama += 1

print(f"A hárommal osztható számok száma: {harommalOszthatoSzamokSzama}")