
#for i in range (1,51,2):
    #print(i)

#lst = [5, 3, 1, 2, 4]
#print(lst)
 
#lst.sort()
#print(lst)  # outputs: [1, 2, 3, 4, 5]
 
#Indices negativos em lista // Matrizes Bidimensionais

#vals = [0, 1, 2]
#vals[0], vals[2] = vals[2], vals[0]
#print(vals) # output: 2,1,0 // O vals [0] atribui seu valor no  vals [2] e o vals [2] vai para o vals [0]


#vals = [0, 1, 2]
#vals.insert(0, 1)
#del vals[1]
 
#print(vals)

#nums = [1, 2, 3]
#vals = nums
#del vals[1:2]
 
#print(vals)

#nums = [1, 2, 3]
#vals = nums[-1:-2]
 
#print(vals)

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print()
 
 #Output - 3,2,1 // o 0 se coloca no indice zero (inicio) e vai empurrando o numero
 # Ex: Entrou o 1, dps o 2, assim sendo 2,1 e dps o 3 e formando 3,2,1  


my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print()
 
my_list = [i for i in range(-1, 2)]
 
print(my_list)