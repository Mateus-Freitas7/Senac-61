
nome = []
cpf = []
endereco = []
email = []
telefone = []
conta = []
saldo = []
data_nascimento = []
tipo_conta = []
agencia = []
senha = []
limite = []

while True:
    opcao = int (input("\nMenu"
                      "\n1 - Cadastrar clientes"
                      "\n2 - Consulta de cadastro"
                      "\n3 - Exclusão de cadastro"
                      "\n4 - Ver saldo"
                      "\n5 - Depósito"
                      "\n6 - Saque"
                      "\n7 - Edição"
                      "\n8 - Sair"
                      "\nEscolha uma opção: "))

    if opcao == 1:
        print("\nCadastrar cliente:")

        nome_cliente = input("Nome cliente: ")
        endereco_cliente = input("Endereço: ")
        telefone_cliente = input("Telefone: ")
        cpf_cliente = input("CPF: ")
        agencia_cliente = input("Agência: ")
        conta_cliente = input("Conta: ")
        saldo_cliente = float(input("Saldo: "))
        data_cliente = input("Data de nascimento: ")
        email_cliente = input("Email: ")
        tipo_cliente = input("Tipo conta: ")
        senha_cliente = input("Senha: ")
        limite_cliente = float(input("Limite de crédito: "))

        nome.append(nome_cliente)
        endereco.append(endereco_cliente)
        telefone.append(telefone_cliente)
        cpf.append(cpf_cliente)
        agencia.append(agencia_cliente)
        conta.append(conta_cliente)
        saldo.append(saldo_cliente)
        data_nascimento.append(data_cliente)
        email.append(email_cliente)
        tipo_conta.append(tipo_cliente)
        senha.append(senha_cliente)
        limite.append(limite_cliente)

        print("Cliente cadastrado com sucesso!")

    elif opcao == 2:
        print("\nConsulta de cadastro")
        consulta = input("Digite o CPF: ")

        if consulta in cpf:
            indice = cpf.index(consulta)

            print(f"Nome: {nome[indice]}")
            print(f"CPF: {cpf[indice]}")
            print(f"Endereço: {endereco[indice]}")
            print(f"Telefone: {telefone[indice]}")
            print(f"Agência: {agencia[indice]}")
            print(f"Tipo de conta: {tipo_conta[indice]}")
            print(f"Conta: {conta[indice]}")
            print(f"Saldo: {saldo[indice]}")
            print(f"Data nascimento: {data_nascimento[indice]}")
            print(f"Senha: {senha[indice]}")
            print(f"Limite: {limite[indice]}")
            print(f"Email: {email[indice]}")
        else:
            print("CPF não encontrado")

    elif opcao == 3:
        print("\nExclusão de cadastro")
        consulta = input("Digite o CPF: ")

        if consulta in cpf:
            indice = cpf.index(consulta)

            nome.pop(indice)
            endereco.pop(indice)
            cpf.pop(indice)
            telefone.pop(indice)
            agencia.pop(indice)
            conta.pop(indice)
            saldo.pop(indice)
            data_nascimento.pop(indice)
            senha.pop(indice)
            limite.pop(indice)
            email.pop(indice)
            tipo_conta.pop(indice)

            print("Cliente removido com sucesso!")
        else:
            print("CPF não encontrado")

    elif opcao == 4:
        print("\nConsulta de Saldo")
        consulta = input("Digite o número da conta: ")

        if consulta in conta:
            indice = conta.index(consulta)

            senha_digitada = input("Senha: ")

            if senha_digitada == senha[indice]:
                print("Saldo:", saldo[indice])
            else:
                print("Senha inválida")
        else:
            print("Conta não encontrada")

    elif opcao == 5:
        print("\nDepósito")
        consulta = input("Digite o número da conta: ")

        if consulta in conta:
            indice = conta.index(consulta)

            valor = float(input("Digite o valor: "))

            if valor > 0:
                saldo[indice] += valor
                print("Depósito realizado com sucesso")
            else:
                print("Valor inválido")
        else:
            print("Conta não encontrada")

    elif opcao == 6:
        print("\nSaque")
        consulta = input("Digite o número da conta: ")

        if consulta in conta:
            indice = conta.index(consulta)

            senha_digitada = input("Senha: ")

            if senha_digitada == senha[indice]:
                valor = float(input("Digite o valor: "))

                if valor > saldo[indice]:
                    print("Saldo insuficiente")
                elif valor <= 0:
                    print("Valor inválido")
                else:
                    saldo[indice] -= valor
                    print("Saque realizado com sucesso")
            else:
                print("Senha inválida")
        else:
            print("Conta não encontrada")
   
  

    elif opcao == 7:
     solicitar_cpf = input("Digite o CPF do cliente:")

     if solicitar_cpf in cpf:
        indice = cpf.index(solicitar_cpf)

        alteracao = int (input("Escolha a opção a ser alterada:""\n1 - Nome" "\n2 - CPF" "\n3 - Endereço""\n4 - Agência""\n5 - Número da conta""\n6 - Email""\n7 - Data de nascimento""\n8 - Tipo de conta""\n9 - Senha""\n10 - Limite de crédito""\nEscolha uma opção:"))

        if alteracao == 1:
            print(f"\nNome atual: {nome[indice]}")

            novoNome = input("Digite o novo nome: ")

            nome[indice] = novoNome

            print(f"O nome foi atualizado, ele agora é: {nome[indice]}")



     if alteracao == 2:
        print(f"\nCPF atual: {cpf[indice]}")

        novocpf = input("Digite o seu novo CPF: ")

        cpf[indice] = novocpf

        print(f"O CPF foi atualizado, ele agora é: {cpf[indice]}")


        
     if alteracao == 3:
        print(f"\nEndereço atual: {endereco[indice]}")

        novoendereco = input("Digite o seu novo endereço: ")

        endereco[indice] = novoendereco

        print(f"O endereço foi atualizado, ele agora é: {endereco[indice]}")


        if alteracao == 4:
            print(f"\nAgênciaço atual: {agencia[indice]}")
            
            novoagencia = input("Digite o seu novo endereço: ")

            agencia[indice] = novoagencia

            print(f"A agência foi atualizada, ela agora é: {agencia[indice]}")

        if alteracao == 5:
            print(f"\nAgênciaço atual: {agencia[indice]}")
            
            novoagencia = input("Digite o seu novo endereço: ")

            agencia[indice] = novoagencia

            print(f"A agência foi atualizada, ela agora é: {agencia[indice]}")
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     '''elif opcao == 8: 
        print("Sistema encerrado.")
        break
     else:
         print("Opção inválida")'''
    
