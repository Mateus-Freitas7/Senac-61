
inserir = 1
visualizar = 2
remover = 3
info5 = "Data de nascimento: 29/10/2000"
info6 = "Telefone:12345678"
opcao = 10
cad = 1

clientes = ["Mateus","João","Gabriel","Lucas","Carlos"]
posicao = [0,1,2,3,4]

while opcao !=0:

    opcao = int(input("\nGERENCIAMENTO -" "\n 1 - Cadastrar clientes" "\n 2 - Visualizar clientes" "\n 3 - Remover clientes" "\n Escolha uma opção:"))
    if opcao==1:
        print("\nInserir clientes")
        cad = int (input("\nDigite usuário:"))
        cad = int (input("\nDigite senha:"))
        info1 = str (input("\nNome do cliente:"))
        info2 = str (input("\nData de nascimento:"))
        info3 = str (input("\nTelefone:"))
        print(cad)
        print(info1)
        print(info2)
        print(info3)
        clientes.append(info1)
        print("\nLista atualizada:",clientes)

    elif opcao==2:
        print("Consultar cliente:")
        nomeconsult = str (input("\nNome cliente:"))
        clientes.index(nomeconsult)
        print("\nCliente:",nomeconsult)
        print("\nInformações:")
        print("\nNome:",nomeconsult)
        print(info5)
        print(info6)


    elif opcao==3:
        remover = str (input("\nNome cliente:"))
        remover2 = int (input("\nNúmero cliente para remoção: "))
        clientes.pop(remover2) 
        print("\nCliente removido:",remover2)
        print("\nLista atualizada:",clientes)

    elif opcao==0:
        print("\nVocê saiu.")