


candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0

while True:
    opcao = int(input("\n1 - Candidato 1:" "\n2 - Candidato 2:" "\n3 - Candidato 3:" "\n4 - Candidato 4:" "\n5 - Digite 5 para sair." "\nEscolha uma opção:"))
    match opcao:
     case 1:
          candidato1 = candidato1+1

     case 2:
      candidato2 = candidato2+1
     case 3:
          candidato3 = candidato3+1
     case 4:
          candidato4 = candidato4+1
     case 5:
          print("Encerrado")
          break
nulo = nulo +1
totalvotos = candidato1+candidato2+candidato3+candidato4 
print("\nCandidato 1:",candidato1)
print("\nCandidato 2:" ,candidato2)
print("\nCandidato 3:" ,candidato3)
print("\nCandidato 4:" ,candidato4)
print("\nTotal votos nulos:",nulo)
print("\nTotal de votos :" ,totalvotos)


        
