
#ele nao tava recebendo valor por conta da variavel opcao que ja estava recebendo 0 // era considerado falso

#opcao tinha que receber um input


opcao = 1

while opcao !=0:

    opcao = int(input("\nCalculadora" "\n 1 - Adição""\n 3 - Subtração" "\n 2 - Multiplicação"  "\n 4 - Divisão" "\n 0 - Sair" "\nEscolha uma opção:"))
    if opcao==1:
        print("\nAdiçao")
        num = int(input("Digite um número:"))
        num2 = int(input("Digite um número:"))
        soma = num+num2
        total = soma
        print("Total Soma:",total)

    elif opcao==2:
        print("\nMultiplicação")
        num = int(input("Digite um número:"))
        num2 = int(input("Digite um número:"))
        mult = num*num2
        total = mult
        print("Total Mult:",total)

    elif opcao==3:
        print("Subtração")
        num = int(input("Digite um número:"))
        num2 = int(input("Digite um número:"))
        sub = num-num2
        total = sub
        print("Total Sub:",total)

    elif opcao==4:
        print("Divisão")
        num = int(input("Digite um número:"))
        num2 = int(input("Digite um número:"))
        div = num/num2
        total = div
        print("Total Div:",total)

    elif opcao==0:
        print("\nEncerrado")
        break
    else:
        print("Opção inválida")


