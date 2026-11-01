a=float(input("Valor:"))
b=float(input("Valor:"))
c=float(input("Valor:"))


if(a==0):
    print("Encerrado")

elif(a**2+b+c<=-1):
    print("A equação não possuí raízes \n Encerrado")
    
elif(a**2+b+c==0):
    print("Possui uma raiz real")

elif(a**2+b+c>=1):
    print("a equação possuí duas raízes.")


#delta = b**2-4.a.c
# se der negativo(Não tem raizes)
# se der positivo faz o calculo
# (-b+delta**0.5)/2*a
# (-b-delta**0.5)/2*a