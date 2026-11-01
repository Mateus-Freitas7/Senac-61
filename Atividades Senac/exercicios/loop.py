

while True:
    try:
        quantidade = int(input("Quantidade:"))
        if quantidade <= 0:
            print("Apenas números positvos")
            continue
        break
        
    except ValueError:
        print("Apenas números!")

for i in range(quantidade):
    print("Olá!")