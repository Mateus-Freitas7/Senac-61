



produto=str(input("Nome do produto:"))

x=float(input("Quantidade:"))

valor=float(input("Valor unitário R$:"))

y=int(input("Desconto a ser aplicado:"))

soma=x*valor
desconto=y/100
dt=desconto*soma
total=soma-dt

print("O produto é:",produto)
print("O valor toal é:",total)
