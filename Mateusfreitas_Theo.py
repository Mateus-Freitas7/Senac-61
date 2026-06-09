

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
    opcao = input(
        "\nMenu"
        "\n1 - Login"
        "\n2 - Cadastrar clientes"
        "\n3 - Consulta de cadastro"
        "\n4 - Exclusão de cadastro"
        "\n5 - Ver saldo"
        "\n6 - Depósito"
        "\n7 - Saque"
        "\n8 - Edição"
        "\n9 - Sair"
        "\nEscolha uma opção: "
    )

    if opcao == '1':
        print("\nLogin Gerente")
        login = input("Digite usuário: ")
        senha_login = input("Digite senha: ")
        print("\nAcesso permitido")

    elif opcao == '2':
        print("\nCadastrar cliente:")

        nome_cliente = input("Nome cliente: ")
        endereco_cliente = input("Endereço: ")
        telefone_cliente = input("Telefone: ")
        cpf_cliente = input("CPF: ")
        agencia_cliente = input("Agência: ")
        conta_cliente = input("Conta: ")
        while True:
            try:
                saldo_cliente = float (input("Saldo: "))
                break
            except:
                print("Apenas números")
        data_cliente = input("Data de nascimento: ")
        email_cliente = input("Email: ")
        tipo_cliente = input("Tipo conta: ")
        senha_cliente = input("Senha: ")

        while True:
            try:

             limite_cliente = float (input("Limite de crédito: "))
             break
            except:
                print("Apenas números")

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

    elif opcao == '3':
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

    elif opcao == '4':
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

    elif opcao == '5':
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

    elif opcao == '6':
        print("\nDepósito")
        
        consulta = input("Digite o número da conta: ")

        if consulta in conta:
            indice = conta.index(consulta)
            while True:
              try:
               valor = float(input("Digite o valor: "))

               if valor > 0:
                   saldo[indice] += valor
                   print("Depósito realizado com sucesso")
                   break
               else:
                print("Valor inválido")
                
              except:
                  print("\nApenas números")
            
        else:
            print("Conta não encontrada")

    elif opcao == '7':
        print("\nSaque")
        consulta = input("Digite o número da conta: ")

        if consulta in conta:
            indice = conta.index(consulta)

            senha_digitada = input("Senha: ")

            if senha_digitada == senha[indice]:
               while True:
                try:
                 valor = float(input("Digite o valor: "))
                 if valor > saldo[indice]:
                    print("Saldo insuficiente")

            

                 else:
                    saldo[indice] -= valor
                    print("Saque realizado com sucesso")
                 break

                except:
                 print("Apenas números")

              

            else:
                print("Senha inválida")

        else:
            print("Conta não encontrada")

    elif opcao == '8':

        solicitar_cpf = input("Digite o CPF do cliente: ")

        if solicitar_cpf in cpf:

            indice = cpf.index(solicitar_cpf)
            print("\nAlteração de dados")
            alteracao = input(
                "\n1 - Nome"
                "\n2 - CPF"
                "\n3 - Endereço"
                "\n4 - Agência"
                "\n5 - Número da conta"
                "\n6 - Email"
                "\n7 - Data de nascimento"
                "\n8 - Tipo de conta"
                "\n9 - Senha"
                "\n10 - Limite de crédito"
                "\nEscolha uma opção: "
            )

            if alteracao == '1':
                print(f"\nNome atual: {nome[indice]}")
                nome_novo  = input("Digite o nome novo:")
                nome[indice] = nome_novo
                print("Nome atualizado!""\nNome novo:",{nome[indice]})

            elif alteracao == '2':
                print(f"\nCPF atual: {cpf[indice]}")
                cpf_novo = (input("Digite o CPF novo:"))
                cpf[indice] = cpf_novo
                print("CPF atualizado!""\nCPF novo:",{cpf[indice]})

            elif alteracao == '3':
                print(f"\nEndereço atual: {endereco[indice]}")
                endereco_novo = (input("\nEndereço novo:"))
                endereco[indice] = endereco_novo
                print("Endereço atualizado!""\nEndereço novo:",{endereco[indice]})

            elif alteracao == '4':
                print(f"\nAgência atual: {agencia[indice]}")
                agencia_nova = (input("Digite a agência nova:"))
                agencia[indice] = agencia_nova
                print("Agência atualizada!""\nAgência nova:",{agencia[indice]})

            elif alteracao == '5':
                print(f"\nConta atual: {conta[indice]}")
                conta_nova = input("\nDigite a conta nova:")
                conta[indice] = conta_nova
                print("Conta atualizada!""\nConta nova:",{conta[indice]})

            elif alteracao == '6':
                print(f"\nEmail atual: {email[indice]}")
                email_novo = (input("Digite o e-mail novo:"))
                email[indice] = email_novo
                print("Email atualizado!""\nEmail novo:",{email[indice]})

            elif alteracao == '7':
                print(f"\nData atual: {data_nascimento[indice]}")
                datanasc_novo = (input("Digite nova data:"))
                data_nascimento[indice] = datanasc_novo
                print("Data atualizada!""\nData nova:",{data_nascimento[indice]})

            elif alteracao == '8':
                print(f"\nTipo atual: {tipo_conta[indice]}")
                tipo_conta_novo = (input("Digite o novo tipo de conta:"))
                tipo_conta[indice] = tipo_conta_novo
                print("Tipo atualizado!""\nNovo tipo de conta:",{tipo_conta[indice]})

            elif alteracao == '9':
                print("senha atual:",senha[indice])
                senha_nova = (input("Digite a nova senha:"))
                senha[indice] = senha_nova
                print("Senha atualizada!""\nSenha nova:",{senha[indice]})

            elif alteracao == '10':
                print("Limite atual:",limite[indice])
                while True:
                    try:
                     limite_novo = float(input("Limite novo:"))
                     limite[indice] = limite_novo
                     print("Limite atualizado!""\nLimite novo:",{limite[indice]})
                     break
                    except:
                        print("Apenas números")

            else:
                print("Opção inválida")

        else:
            print("CPF não encontrado")

    elif opcao == '9':
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida")
        