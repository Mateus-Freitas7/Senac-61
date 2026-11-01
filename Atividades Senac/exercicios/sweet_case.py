
salario = 1000
dep = int(input("Número de dependentes:"))

match dep:
    case 1:
        sal = salario + (salario*5)/100
        print("Seu salário  pós ajuste:",sal)