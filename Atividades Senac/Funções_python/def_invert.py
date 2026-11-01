
def invert(nome,sobrenome):
    nomeInv = sobrenome+","+nome
    return nomeInv
while True:
    try:
        nome = input("Nome:")
        sobrenome = input("Sobrenome:")
        break
    except:
        print("Apenas letras")
invertido = invert(nome,sobrenome)
print("Olá" ,invertido,)