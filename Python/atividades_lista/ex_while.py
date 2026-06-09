

###fazer um algoritimo que receba n números e some - os até que o usuário digite 0 para sair 
#média dos números digitados

quant=0
soma=0

num=int(input("digite um número:"))
while num != 0:
    soma+=num
    quant+=1
    print("valor atual soma:",soma,"quant:",quant)

    
    num=int(input("digite um número:"))


media = soma / quant
print("Média",media)


