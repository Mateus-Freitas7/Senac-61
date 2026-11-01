

usuario = "admin"
senha = 1234
tentativas = 3

while True:

    while True:
        try:
            usuario_digitado = (input("Digite seu usuário:"))
            break
        except:
            print("Apenas letras!")
    while True:
        try:
            senha_digitada = int (input("Digite sua senha:"))
            break
        except:
            print("Apenas números")

    if senha_digitada != senha or usuario_digitado != usuario:
        tentativas -= 1
        print(f"Usuário ou senha incorretos \nte restam {tentativas} tentativas")
        

    if tentativas == 0:
        print("Acesso negado!")
        break
    

    if (senha_digitada == senha) and (usuario_digitado == usuario):
        while True:

            while True:
                    try:
                        menu = int (input("\n1 - Dados do usuário \n2 - Alterar dados \n3 - Logout \n4 - Sair \nEscolha uma opção"))
                        break
                    except:
                        print("Apenas as opções acima!")
            
            match menu:
                    case 1:
                        print(f"\nDados do usuário \nUsuário:{usuario} \nSenha:{senha}")
                    case 2:
                        consulta = int(input("Digite sua senha para poder efetuar alteração:"))
                        if consulta == senha:
                            print(f"\nAlterar dados \nSua senha atual é:{senha}")
                            new_senha = int(input("Nova senha:"))
                            senha = new_senha
                            print("Senha alterada.")
                        else:
                            print("Senha incorreta")

                    case 3:
                        print("Voltando ao menu...")
                        break

                    case 4:
                        print("Encerrando...")
                        exit()