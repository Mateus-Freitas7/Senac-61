
def Hanoi(n,origem,auxiliar,destino):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return 1
    

    movimentos = 0

    movimentos += Hanoi(n-1,origem,destino,auxiliar)

    print(f"Mover disco {n} de {origem} para {destino}")
    movimentos += 1
    
    movimentos += Hanoi(n-1,auxiliar,origem,destino)
    return movimentos

n = int(input("Digite o número de discos:"))

total = 2**n -1
print(f"\nTotal de movimentos: {total}\n")
print("Passo a Passo:")
print("-"*30)
Hanoi(n,"A","B","C")
print("-"*30)


