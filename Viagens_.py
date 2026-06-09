
destino = []
valor = []
vagas = []
indice = [destino,vagas,valor]

while True:
    opcao = int (input("\n1 - Cadastro de destino" "\n2 - Destinos disponíveis" "\n3 - Compra de passagem"  "\n4 - Encerrar sistema" "\nEscolha uma opção:"))

    match opcao:
        case 1:
            quantidade = int (input("Quantidade de destinos que serão cadastrados:"))
            for i in range(quantidade):
             
             print("Cadastro de destino")
             while True:
                try:
                    nome_destino = (input("Nome do destino:"))
                    break
                except:
                    print("Apenas letras!")
                    while True:
                     try:
                        valor_passagem = float (input("Valor da passagem:"))
                        quantidade_vagas = int (input("Quantidade de vagas:"))
                        break
                     except:
                        print("Apenas números!")

            destino.append(nome_destino)
            valor.append(valor_passagem)
            vagas.append(quantidade_vagas)
            

        case 2:
            print("Destinos disponíveis")
            for i in destino:
               print(i)
            else:
               print("Destino não existente!")
               
        case 3:
                print("Compra de passagem")
                consulta = (input("nome do destino qe deseja comprar:"))
                if consulta in destino:
                   indice = destino.index(consulta)
                   if vagas[indice] <=0:
                      print("Vagas esgotadas!")
                   else:
                        print("Valor dapassagem:",valor[indice])
                        while True:
                         try:
                            compra = int (input("Deseja comprar quantas passagens para o destino:",{destino[indice]}))
                            break
                         except:
                            print("Apenas números!")
                        if compra <=0:
                         print("Volte ao menu.")
                        elif compra > vagas[indice]:
                         print("Não há vagas suficientes")
                        else:
                         total = compra*valor[indice]
                        print("O valor total das passagens:",total)
                        print("Cancelar ou Confirmar")
                        escolha = (input("Opção:"))
                        if escolha == "Confirmar":
                           print("Pagamento concluído!")
                           vagas[indice] -= compra
                        elif escolha == "Cancelar":
                           print("Pagamento cancelado")
                        else:
                            print("Essa opção não existe.")
                
                else:
                   print("Destino não encontrado!")          
                   
        case 4:
            print("Consulta de vagas restantes")
            consulta = (input("Destino que deseja consultar quantidade de vagas:"))
            if consulta in destino:
               vagas[indice] -= compra
               print("Quantidade de vagas restantes:",{vagas[indice]})

        case 4:
          print("Sistema encerrado!")

           