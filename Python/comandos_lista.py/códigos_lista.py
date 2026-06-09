

lista=[12,11,13,14,15,16,70,5,99]


print(lista[-1])### print ultimo elemento da lista

print(lista) ### print lista inteira

lista.sort()  ### ordenando a lista em ordem crescente

print(lista)

lista.sort(reverse=True) ### ordem decrescente

print(lista)


lista2=[] ### lista vazia

coisa= input("digite algo:")

lista2.append(coisa)

print(lista2)

lista.pop() ### excluir o ultimo elemento da lista
print(lista)
lista.pop()
print(lista)

lista.insert(2,23)
print(lista)


