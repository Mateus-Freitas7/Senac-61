

pao = float (input("Qual o preço do pão:"))
preco = pao

for i in range (1,51):
    print("----------")
    print(i,f"- R${pao:.2f}")
    pao+= preco
    