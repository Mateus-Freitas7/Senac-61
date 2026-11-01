
nome = []
ingresso = []
quantidade = []
valor= []

pista = 50
vip = 120
camarote = 250

indice = [nome,ingresso,quantidade,valor]

while True:
    try:
       n  = int (input("Quantas Compras você deseja Fazer::"))
       break
    except:
       print("Apenas Números!")
cont=0
for i in range (n):
   cont+=1
   print('Compra ',cont)
   nome_cliente = (input("Nome:"))
   nome.append(nome_cliente)
   
   while True:
      try:
       tipo_ingresso = int (input("\n1 - Pista" "\n2 -  VIP" "\n3 - Camarote" "\nEscolha uma opção:"))
       break
      except:
       print("Apenas as opções disponíveis do menu!")
   match tipo_ingresso:
      case 1:
        pista = 50
        valor.append(pista)
        ingresso.append("Pista")

      case 2:
         vip = 120
         valor.append(vip)
         ingresso.append("VIP")

      case 3:
         camarote = 250
         valor.append(camarote)
         ingresso.append("Camarote")
   if 1< tipo_ingresso >3:
      print("Esta opção nao existe")
   while True:
      try:
         quantidade_ingresso = int (input("Quantidade:"))
         break
      except:
         print("Apenas números!")
   quantidade.append(quantidade_ingresso)

   consulta = (input("Confirme seu nome:"))
   if consulta in nome:
      indice = nome.index(consulta)
      total = valor[indice] * quantidade[indice]

      escolha = (input("\n1 - Confirmar" "\n2 - Cancelar"))
      if escolha == '1':
            print("Resumo de compra")
            print("Nome:",nome[indice])
            print("Quantidade:",quantidade[indice])
            print("Valor por unidade:",valor[indice])
            print("Valor total da compra:",{total})
            print("Compra finalizada!!!")

      elif escolha == '2':
            print("Compra cancelada.")
      else:
            print("Esta opção não existe!!!")

   else:
      print(f"O nome {consulta} não existe.")
      

            
        


         
    


             
       




