

#End = // ele deixa o print numa linha só // Ex: 1,2,3 // e não 
                                                            #1
                                                            #2
                                                            #3


termo = int(input("Série até que número:"))
primeiro = 0
print(primeiro, end ="")
segundo = 1

for i in range(1,termo):
    print(",",segundo, end ="")
    terceiro = primeiro + segundo #Recebe a soma 
    primeiro = segundo
    segundo = terceiro


 

