

pessoas = int (input("Quantidade de pessoas:"))
idade_pessoas = []

for i in range(10):
    idade = int(input("Digite sua idade:"))
    idade_pessoas.append(idade)
print(f"a Média de idade é:{sum(idade_pessoas)/pessoas}")


if 0 <=idade>=25:
        print("Jovem")

elif 26 <=idade>60:
        print("Adulto")

elif idade >=60:
    print("Idoso")

   

    


    
