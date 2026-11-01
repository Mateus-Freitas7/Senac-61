#hello(input("Digite seu nome:"))
#hello("Mateus")
#hello("João")


#def hello(nome,idade):
    #print("Olá" ,nome, "\nsua idade é:" ,idade)

#x = input("Nome:")
#y = input("Idade:")

#hello(x,y)


def calculo_pagamento(qnt_horas,valor_hora):
    horas = float (qnt_horas)
    taxa = float (valor_hora)
    if horas <=40:
        salario = horas*taxa
    else:
        h_excd = horas - 40
        salario = 40*taxa+(h_excd*(1.5*taxa))
    print(salario)


