quantidade = int(input("Quantidade:"))

contador = 0
soma  = 0

numeros = []

while contador < quantidade:
    numero = int(input("N:"))
    numeros.append(numero)

    #print(numero,contador)
   

    #contador = contador +1
    contador+= 1
    
    #soma = soma  + numero

    soma+= numero

print("O maior valor digitador foi:",max(numeros))
print("resultou na soma do valor:",soma)