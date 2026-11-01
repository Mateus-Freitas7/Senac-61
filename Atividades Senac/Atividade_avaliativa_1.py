
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
    opcao = int(input("\nMenu"
                      "\n1 - Login"
                      "\n2 - Cadastrar clientes"
                      "\n3 - Consulta de cadastro"
                      "\n4 - Exclusão de cadastro"
                      "\n5 - Ver saldo"
                      "\n6 - Depósito"
                      "\n7 - Saque"
                      "\n8 - Sair"
                      "\nEscolha uma opção: "))
    if opcao==1:
        print("\nLogin Gerente")
        login = (input("Digite usuário:"))
        senha_login = (input("Digite senha:"))
        
    
    
    elif opcao == 2:
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

    elif opcao == 3:
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

    elif opcao == 4:
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

    elif opcao == 5:
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

    elif opcao == 6:
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

    elif opcao == 7:
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

    elif opcao == 8:
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida")
