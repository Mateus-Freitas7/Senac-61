consulta = []
restaurante = []
nome_restaurante = []
quant_funcionarios = []
quant_atendidos = []
total_faturamento = []
total_atendidos = []
total_entregas = []
total_cancelados = []
total_itens = []
endereco_restaurante = []
media_nota = []
while True:
        opcao = input("\n1 - Cadastrar Restaurante" "\n2 - Buscar restaurante pelo nome" "\n3 - Exibir relatório" "\n4 - Mostrar estatícas gerais" "\n5 - Atualizar dados do restaurante" "\n6 - Remover restaurante""\n7 - Encerrar sistema" "\nEscolha uma opção:")
        if opcao == '1':
            print("Cadastro de restaurante")
            while True:
                try:
                 restaurante = int (input("Quantidade de restaurantes:"))
                 break
                except :
                   print("Apenas números!")

                for i in range (restaurante):  
                   nome = (input("Nome do restaurante:"))
                   endereco = (input("Endereço:"))

            while True:
                 try:
                  funcionarios = int (input("Quantidade de funcionários:"))
                  break
                 except ValueError:
                  print("Número inválido!")

            while True:
             try:
              atendidos = int (input("Quantidade de clientes atendidos no mês:"))
              break
             except ValueError:
                 print("Apenas números!")

            while True:
                try:
                    faturamento = float (input("Faturamento mensal:"))
                    break
                except ValueError:
                 print("Inválido!")

            while True:
                try:
                 entregas = int (input("Quantidade de pedidos entregues:"))
                 break
                except ValueError:
                 print("Inválido!")
            while True:
                try:
                 cancelados = int (input("Quantidade de pedidos cancelados:"))
                 break
                except ValueError:
                 print("Inválido!")
                 
            while True:       
               try:
                nota_cliente = float (input("Nota média clientes:"))
                if 0   <=nota_cliente <= 10:
                   break
                else:
                 print("Nota de 0 a 10")
                
               except ValueError:
                 print("Inválido")

            while True:
               try:     
                itens_cardapio = int (input("Quantidade de pratos no cardápio:"))
                break
               except ValueError:
                print("Inválido")

            nome_restaurante.append(nome)
            endereco_restaurante.append(endereco)
            quant_funcionarios.append(funcionarios)
            quant_atendidos.append(atendidos)
            total_faturamento.append(faturamento)
            total_entregas.append(entregas)
            total_cancelados.append(cancelados)
            media_nota.append(nota_cliente)
            total_itens.append(itens_cardapio)

            print("Cadastro feito!")

        elif opcao == '2':
            print("Consulta de restaurante")
            consulta = (input("Nome do restaurante que deseja buscar:"))

            if consulta in nome_restaurante:
                indice = nome_restaurante.index(consulta)
                print(f"\nNome: {nome_restaurante[indice]}")
                print(f"\nEndereço: {endereco_restaurante[indice]}")
                print(f"\nQuantidade de funcionários: {quant_funcionarios[indice]}") 
                print(f"\nQuantidade de clientes atendidos no mês: {quant_atendidos[indice]}")
                print(f"\nFaturamento mensal: {total_faturamento[indice]}")
                print(f"\nQuantidade de entregas {total_entregas[indice]}")
                print(f"\nQUantidade de pedidos cancelados:{total_cancelados[indice]}")
                print(f"\nNota dos clientes: {media_nota[indice]}")
                print(f"\nItens no cardápio:{total_itens[indice]}")
            
        elif opcao == '3':
            print("Relatório detalhado")
            consulta = (input("Nome para busca de relatório:"))
            if consulta in nome_restaurante:
                indice = nome_restaurante.index(consulta)

                if faturamento > '10000':
                   print(nome_restaurante,"com mais de R$100.000 de faturamento")
                else:
                   print("Nenhum restaurante com mais de R$ 100.000 de faturamento")

            print("Maior número de entregas:",max(total_entregas[indice]))

            print("Total de pedidos cancelados:",{total_cancelados[indice]})

            print("Nota de clientes:",{media_nota[indice]})

            if total_itens > '100':
               print("Cardápio com mais de 100 itens!")
            else:
               print("Possui menos de 100 itens no cardápio.")



        elif opcao == '4':
            print("Estatíscas gerais")


        elif opcao == '5':
           print("Atualizar dados")
           consulta = input("Nome do restaurante que deseja atualizar os dados")

           if consulta in nome_restaurante:
              indice = nome_restaurante.index(consulta)
              print("\nEscolha o que deseja mudar no menu abaixo:" "\n1 - Nome" "\n2 - Endereco" "\n3 - Quantidade de funcionários" "\n4 - Itens no cardápio")
              
              if opcao == '1':
               print(f"Nome atual:",{nome[indice]})
               nome_novo = (input("Nome novo:"))
               nome[indice] = nome_novo
               print("Nome atualizado!")

           elif opcao == '2':
             print("Endereço atual:",{endereco[indice]})
             endereco_novo = (input("Digite novo endereço:"))
             endereco[indice] = endereco_novo
             print("Endreço atualizado!")

           elif opcao == '3':
            print("Quantidade de funcionários atual:",{funcionarios[indice]})
            ajuste_funcionarios = (input("Reajuste de funcionários:"))
            funcionarios[indice] = ajuste_funcionarios
            print("Quantidade de funcionários atualizado!")


           elif opcao == '4':
            print("Número de itens no cardápio atualmente:",{itens_cardapio[indice]})
            itens_atualizado = (input("Nova quantidade de itens:"))
            itens_cardapio[indice] = itens_atualizado
            print("Número atualizado!")

        elif opcao == '6':
           print("Remoção de restaurante")
           consulta = (input("Nome do restaurante que deseja remover:"))
           if consulta in nome_restaurante:
              indice = nome_restaurante.index(consulta)
              nome_restaurante.pop(indice)
              endereco_restaurante.pop(indice)
              quant_funcionarios.pop(indice)
              quant_atendidos.pop(indice)
              total_faturamento.pop(indice)
              total_entregas.pop(indice)
              total_cancelados.pop(indice)
              media_nota.pop(indice)
              total_itens.pop(indice)
              print("Remoção feita!")  

           
 
              
