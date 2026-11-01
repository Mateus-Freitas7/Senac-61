
cidades = []
indices = []

qtd = int(input("Quantas cidades deseja cadastrar? "))

for i in range(qtd):
    print(f"Cidade {i+1}")
    codigo = int(input("Código da cidade: "))
    nome = input("Nome da cidade: ")
    estado = input("Estado: ")
    veiculos = int(input("Número de veículos: "))
    acidentes_com = int(input("Acidentes com vítimas: "))
    acidentes_sem = int(input("Acidentes sem vítimas: "))
    embriagado = int(input("Acidentes com motorista embriagado: "))
    total_acidentes = acidentes_com + acidentes_sem
    cidades.append([codigo,nome,estado,veiculos,acidentes_com,acidentes_sem,embriagado])
    indices.append(total_acidentes)
maior = max(indices)
menor = min(indices)

for i in range(len(indices)):
    if indices[i] == maior:
        cidade_maior = cidades[i][1]
    if indices[i] == menor:
        cidade_menor = cidades[i][1]
print("Maior índice de acidentes:", maior)
print("Cidade:", cidade_maior)
print("Menor índice de acidentes:", menor)
print("Cidade:", cidade_menor)
soma_veiculos = 0

for i in range(len(cidades)):
    soma_veiculos += cidades[i][3]
media = soma_veiculos / qtd
print("Média de veículos:", media)
print("Total de veículos:", soma_veiculos)
lista_veiculos = []

for i in range(len(cidades)):
    lista_veiculos.append(cidades[i][3])
maior_veiculo = max(lista_veiculos)
menor_veiculo = min(lista_veiculos)

for i in range(len(cidades)):
    if cidades[i][3] == maior_veiculo:
        print("Cidade com mais veículos:", cidades[i][1])
    if cidades[i][3] == menor_veiculo:
        print("Cidade com menos veículos:", cidades[i][1])
soma_acidentes = 0
contador = 0

for i in range(len(cidades)):
    if cidades[i][3] < 2000:
        soma_acidentes += cidades[i][4] + cidades[i][5]
        contador += 1
if contador > 0:
    media_acidentes = soma_acidentes / contador
    print("Média de acidentes nas cidades com menos de 2000 veículos:", media_acidentes)
total_com = 0
total_sem = 0

for i in range(len(cidades)):
    total_com += cidades[i][4]
    total_sem += cidades[i][5]

print("Total de acidentes:", total_com + total_sem)
print("Com vítimas:", total_com)
print("Sem vítimas:", total_sem)
total_embriagado = 0

for i in range(len(cidades)):
    total_embriagado += cidades[i][6]
print("Acidentes com motorista embriagado:", total_embriagado)