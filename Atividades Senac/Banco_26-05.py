
saldo_cliente = []
nome_cliente = []
indice = [saldo_cliente,nome_cliente]
while True:
    opcao = int (input("\n1 - Cadastro"  "\n2 - Depositar" "\n3 - Saque" "\n4 - Consultar saldo" "\n5 - Encerrar sistema" "\nEscolha uma opção:"))
    match opcao:
        case 1:
            print("Cadastro")
            nome = (input("Digite seu nome:"))

            while True:
                try:
                    saldo = int (input("Saldo inicial:"))
                    break

                except:
                    print("Apenas números")
                    
            nome_cliente.append(nome)
            saldo_cliente.append(saldo)
            print("Cadastro realizado!")
           
            

        case 2:
            print("Depósito")
            consulta = (input("Nome para autorizar depósito:"))
            if consulta in nome_cliente:
             indice = nome_cliente.index(consulta)

             while True:
                try:
                    deposito = int (input("Valor a ser depositado:"))
                    break

                except:
                    print("Apenas números")
             saldo[indice] += deposito  
             print("Valor depositado:",deposito)    
            print("Depósito realizado!")

            
            

        case 3:
            print("Saque")
            consulta = (input("Nome para autorizar saque:"))
            if consulta in nome_cliente:
             indice = nome_cliente.append(consulta)

             while True:
                try:
                    saque = (input("Valor do saque:"))
                    break
                       
                except:
                    print("Apenas números!")
          
                    if saque > saldo[indice]:
                        print("Saldo insuficiente!")

                    else:
                        saldo[indice] -= saque
                        print("valor sacado:")
                        print("Saque realizado!")
                        
        case 4:
            print("Consulta de saldo")
            consulta = (input("Nome para consulta de saldo:"))
            indice = nome_cliente.index(consulta)
            print("Saldo atual:" ,{saldo_cliente[indice]})
            
        case 5:
            print("Sistema encerrado.")
            break
            



            

