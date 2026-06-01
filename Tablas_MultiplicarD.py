print("Tablas de multiplicar")
for i in range(1, 11):
    print(f"\nTabla del {i}:")
    for j in range(1, 11):
        res = i * j 
        print(f"{i} X {j} = {res}")