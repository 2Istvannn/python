print("Kérem adja meg hány elemű a számpiramis: ")
piramis: int = int(input())

for i in range(piramis, 0, -1): 
    print(end="  " "\n")
       
    for i in range(i, 0, -1):
        print(" ", i, end="   ")
        
  