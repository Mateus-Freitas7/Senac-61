
# # numero = int(input("N:"))
# # salto = int(input("S:"))
# contador = int(input("N:"))

# while contador >= 0:
#     print(contador)
#     contador = contador -1



# quantidade = int(input("Q:"))

# contador = 0

# totnegativos = 0
# totpositivos = 0

# while contador < quantidade:

#     numero = int(input("N:"))
#     contador = contador +1

#     if numero > 0:
#         totpositivos = totpositivos +1

#     elif numero < 0:
#         totnegativo = totnegativos +1
        
# print("Números positivos:",totpositivos)

# print("números negativos:",totnegativos)


# num = int(input("Número que deseja fazer tabuada:"))

# contador = 1

# while contador < 11:
#     r = num*contador
#     print(num,"x" ,contador, "=",r)
#     contador = contador +1




# while True:
#     fatorial = int(input("Número:"))
#     contador = fatorial
#     soma = 1
#     while contador >= 1:
#         soma = soma*contador
#         print(contador,  end="x")
#         contador -=1

        
#     print("\nValor total do fatorial de ",fatorial,"é",soma)

#     resposta = input("Quer continuar?") 

#     if resposta == "n":
#         print("Encerrado")
#         break

numero = int(input("N:"))

contador = 1
contDiv = 0

while contador < numero:
   
    

    if ( numero % contador  == 0):
        contDiv +=1 
    if contDiv >2:
        print("O número",numero,"não é primo.")
        break
    contador +=1
else:
    print("O número",numero,"é primo e é divisivel",contDiv,"vezes")
    

