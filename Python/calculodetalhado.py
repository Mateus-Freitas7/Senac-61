
nome=str(input("Nome do cliente:"))

pro=float(input("Valor: R$"))

pro2=float(input("Valor: R$"))

pro3=float(input("Valor: R$"))



soma=pro+pro2+pro3
print("Total Da compra:",soma)


med=soma/3
print("Média de preços:",med)



desc=12/100
vldesc=soma*desc
vlt=soma+vldesc
print("Valor com 12 de imposto:",vlt)



desc2=5/100
vldesc2=vlt*desc2
vlt2=vlt-vldesc2
print("Valor com 5 de desconto:",vlt2)



print("RELATÓRIO  \nValor com imposto:",vlt,"\nValor com desconto:",vlt2)