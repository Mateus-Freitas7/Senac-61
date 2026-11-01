



# resposta = (input("Já arummou o quarto?[S/N]"))

# while resposta != "S":
#         print("Você está de castigo!")
#         resposta = (input("Já arummou o quarto?[S/N]"))


# if resposta == "S":
#         print("seu castigo acabou.")



# contador = int(input("Número que deseja fazer contagem decrescente:"))
# salto = int(input("Número de passo que deseja dar:"))

# while contador >= 0:
#      print(contador)
#      contador = contador - salto
   
# contador = 0

# valor = int(input("Quer contar até que valor?"))

# while contador < valor:
#     print(contador)
#     contador = contador +1



# #Soma de números
# quantidade = int(input("Quantidade:"))

# contador = 0
# soma  = 0

# numeros = []

# while contador < quantidade:
#     numero = int(input("N:"))
#     numeros.append(numero)

#     #print(numero,contador)
   

#     contador = contador +1
    
#     soma = soma  + numero

# print("O maior valor digitador foi:",max(numeros))
# print("resultou na soma do valor:",soma)

# contador = 1 
# quantidade = int(input("Quantas vezes você quer converter?"))
# while contador <= quantidade:
#     real = int(input("Valor para converter em dólar:"))
#     dolar = real//2.20
#     print(f"O valor",real,"em reais vira",dolar,"em dolár")

#     contador = contador +1

#Contador inteligente
# inicio = int(input("Início:"))
# fim = int(input("Fim:"))
# if inicio>fim:
#     while inicio>=fim:
#         print(inicio)
#         inicio -= 1
# else:
#     while inicio <= fim:
#         print(inicio)
#         inicio +=1


quantidade = int (input("Quantos alunos a sala tem?"))
cont = 1
alunos = []
notas = []
while cont <= quantidade:
    aluno = input(f"Aluno {cont}:")
    nota = int(input(f"Nota de {aluno}:"))
    alunos.append(aluno)
    notas.append(nota)
    cont = cont +1
    
indice = notas.index(max(notas))
print("Melhor nota e aproveitamento foi do aluno",alunos[indice],"com a nota",notas[indice])


    