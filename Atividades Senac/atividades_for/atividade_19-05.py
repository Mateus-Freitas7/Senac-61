

pao = float (input("Qual o preço do pão:"))
preco = pao
quantidade = int(input("Quantidade que deseja levar:"))
for i in range (1,quantidade):
    print("----------")
    print(f"{i} - R${pao:.2f}")
    pao += preco
    