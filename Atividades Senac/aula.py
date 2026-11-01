#reais = int(input("Quantos reais eu tenho?"))
#print(reais)
#dolar = reais/2.20

#print("Posso ter:",dolar)

#temperatura = float (input("Qual é a temperatura:"))

#print(temperatura)

#c = (temperatura - 32) / 1.8
#print("Seria em celsius:",c)

#preco = int(input("Qual o preço do produto:"))
#print(preco)
#valor_imposto = (preco*20)/100
#print("O imposto será de:",valor_imposto)
#preco_atual = preco+valor_imposto
#print("Preço do produto:",preco_atual)

#emprestimo = int(input("Valor do emprestimo:"))
#parcelas = int(input("Quantidade de parcelas:"))
#juros = (emp#restimo*20)/100
#preco_juros #= emprestimo+juros
#print("Preço do empres#timo com juros:",preco_juros)
#preco_parcela =  prec#o_juros/parcelas
#print("Você irá pagar",parcelas,"parcelas de:",preco_parcela)

while True:
    opcao = int(input("\n1 - de 0 a 10 \n2 - ordem descrecente \n3 - Sair \nEscolha uma opção:"))

    match opcao:
        case 1:
           
            for i in range(1,52,2):
                print(i)
               
        case 2:
            contador = 0
            numero = int(input("Número que deseja fazer contagem decrecente:"))
            for i in range(numero,0,-1):
                print(i)
        case 0:
            print("Encerrado")
            break


 # O primeiro número dentro do parenteses é o núm unicial, o fim e dps o passo que ele irá dar
