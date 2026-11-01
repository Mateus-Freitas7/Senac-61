

#For com Range = Laço de repetição
#  Sempre começa do 0
# 2 = Ínicio Ex: // 12 número total // 2 quantidade Ex: de 2 em 2


#for i in range (2,12,2):
   # print("\ncontador:",i)


#for i in range (5): #Loop aninhado
    #for j in range(6):
        #print(i,j)

for i in range (1,11):
    print("---------")
    print("Tabuada do ",i)
    print("---------")
    
    for j in range (1,11):
        mult = i*j # Realiza a tabuada num loop aninhado
        print(i,"X",j,"=",mult)
