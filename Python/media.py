n1=float(input("digite a nota 1:"))
n2=float(input("digite a nota 2:"))
n3=float(input("digite a nota 3:"))
n4=float(input("digite a nota 4:"))
media=(n1+n2+n3+n4)/4
if media>= 5.00:
    print(f"Média:{media} - Aprovado")

elif media<6 and media>=4.00:
    print(f"Média:{media} - Exame")

else:
    print(f"Média:{media} - Reprovado")
