
#Contador de votos
#Para fazer a contagem sobre um elemento basta usar o nome da variavel e somar por +1 // Ex: candidato = candidadto+1
#Assim cria a contagem

sair = 1
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
totalvotos = 0


while sair != 0:
    sair = int(input("\n1 - Candidato 1:" "\n2 - Candidato 2:" "\n3 - Candidato 3:" "\n4 - Candidato 4:" "\n0 - Digite 0 para sair" "\nEscolha uma opção:"))


    if sair==1:
           candidato1 = candidato1+1
           print("\nQuantidade:",candidato1)

    elif sair==2:
         candidato2 = candidato2+1
         print("\nQuantidade:",candidato2)
    elif sair==3:
        candidato3 = candidato3+1
        print("\nQuantidade:",candidato3)

    elif sair==4:
         candidato4 = candidato4+1
         print("\nQuantidade:",candidato4)
   
    elif sair==0:
        print("Encerrado")
        totalvotos = candidato1+candidato2+candidato3+candidato4 
        print("\nCandidato 1:",candidato1)
        print("\nCandidato 2:" ,candidato2)
        print("\nCandidato 3:" ,candidato3)
        print("\nCandidato 4:" ,candidato4)
        print("\nTotal votos nulos:",nulo)
        print("\tTotal de votos :" ,totalvotos)
      
else:
    nulo = nulo+1
        
