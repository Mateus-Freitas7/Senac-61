salarioatual=float(input("Salário Atual:"))


if(salarioatual<500):
    reajuste=salarioatual+(salarioatual*15/100)
    print("Salário 1 - Reajuste:",reajuste)

elif(salarioatual>=500) and (salarioatual<=1000):
    reajuste=salarioatual+(salarioatual*10/100)
    print("Salário 1 - Reajuste:",reajuste)

else:
    reajuste=salarioatual+(salarioatual*5/100)
    print("Salário 1 - Reajuste:",reajuste)


