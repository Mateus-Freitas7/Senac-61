
preco=6.29

distancia=float(input("Distância:"))
consumo=float(input("Consumo do carro km:"))



litro=distancia/consumo
print("Qantidade de lt  necessários:",litro)


custo=litro*preco
print("Custo total:",custo)



print("RELATORIO \nLitros necessários:",litro,"Custo total da viagem:",custo)