

cpf = []


while True:
    opcao = (input("\n Menu " "\n1 - Cadastro" "\n2 - Consulta" "\n3 - Remover" "\n4 - Ediçao de dados" "\nEscolha uma opção:"))
    if opcao=='1':
        print("Cadastro de cliente")
        cpf_cliente =(input("Digite o cpf:"))
        cpf.append(cpf_cliente)

    elif opcao=='2':
        print("Consulta")
        consulta = (input("Digite o cpf para busca:"))
        if consulta in cpf:
         indice = cpf.index(consulta)
         print({cpf[indice]}) # Pega o cpf que foi salvo no cadastro

    elif opcao=='3':
        print("Remover")
        consulta = (input("Cpf do cliente que deseja remover")) 
        if consulta in cpf:
         indice = cpf.index(consulta) #Pega a posição
         cpf.pop(indice) #Remove

         print("Removido")

    elif opcao == '4':
     solicitar_cpf = input("Digite o CPF do cliente:")

     if solicitar_cpf in cpf: #Solicita para ver se é o mesmo cpf
        indice = cpf.index(solicitar_cpf)

        alteracao = (input("Escolha a opção a ser alterada:""\n1 - Nome" "\n2 - CPF" "\n3 - Endereço""\n4 - Agência""\n5 - Número da conta""\n6 - Email""\n7 - Data de nascimento""\n8 - Tipo de conta""\n9 - Senha""\n10 - Limite de crédito""\nEscolha uma opção:"))

        if alteracao == '1':
            print(f"\nCPF atual: {cpf[indice]}") # Pega o cpf cadastrado

            cpf_novo = input("Digite o novo CPF: ")

            cpf[indice] = cpf_novo #Muda o antigo para o novo

            print(f"O CPF foi atualizado, ele agora é: {cpf[indice]}")

