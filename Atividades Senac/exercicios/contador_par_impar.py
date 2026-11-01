

terminou = False 

par = impar = 0
while (not terminou):
    numero = int (input("Digite um número, ou zero para terminar:"))
    if numero == 0:
        terminou = True
    else:
        if numero % 2 == 0:
            par += 1
        else: 
            impar += 1            
            
print(f"Quantidade de valores digitados e seus respectivos tipos: \nPar:{par} \nÌmpar:{impar}")