#Recebe 5 números e depois os soma e  a média deles 

numero = 0
for i in range(5):
    numero += float (input("Digite um número:"))
media = numero/5

print("Soma dos números:",numero)
print("Média dos numéros",media)
