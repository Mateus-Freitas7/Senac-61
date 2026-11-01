
#numero = int(input("N:"))
#contador = 100

#while contador > numero:
    #contador-= 10
   #print(contador)
#Enquanto o contador for menor que o número inserido ele vai somar de 1 em 1 até chegar no valor inserido 

# valor = int(input("Digite um valor:"))

# if (valor % 2 == 1):
#     valor -= 1
#     for i in range(valor,-1,-2):
#         print(i)

# elif (valor % 2 == 0):
#     valor -= 1
#     for i in range (valor,0,-2):
#         print(i)



# tot0e10 = 0
# soma = 0
# somaip = 0
# totimpares = 0

# for i in range (1,6):

#     valor = int(input(f"Valor {i}:"))

#     if (valor >= 0) and (valor<=10):
#         tot0e10 += 1
#         soma = soma + valor

#     if (valor % 2 == 1):
#         totimpares +=1
#         somaip = somaip + valor

# print(f"Foram {tot0e10} valores entre 0 e 10 e sua soma {soma}")
# print(f"Quantidade de números ímpares {totimpares} e sua soma {somaip}")

# for c1 in range (1,4):
#       for c2 in range(1,4):
#           print(c1,c2)


n = int(input("número:"))
primeiro , segundo = 0 , 1

for i in range(n):
    print(primeiro,end=",")
    primeiro , segundo = segundo , primeiro + segundo
    