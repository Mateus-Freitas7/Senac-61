pro1=float(input("Produto 1: R$"))

pro2=float(input("Produto 2: R$"))

pro3=float(input("Produto 3: R$"))

pro4=float(input("Produto 4: R$"))

pro5=float(input("Produto 5: R$"))

soma=pro1+pro2+pro3+pro4+pro5
v2=(soma*10/100)
vt=(soma*10/100)-soma

print("Desconto á vista:",v2)
print("Valor total:",vt)

c1=5/100
c2=c1*soma
cl=soma-c2

print("Desconto no cartão:",c2)
print("Valor total:",cl)


parce=soma
print("Parcelado:")
print("Sem desconto.")
print("Valor total parcelado:",parce)