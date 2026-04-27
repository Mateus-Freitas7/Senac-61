print("-- Resevartório de Água --")

altura=float(input(" Digite a altura (cm):"))

largura= float(input(" Digite a largura (cm): "))

comprimento=float(input("Digite o comprimento (cm):"))
                  
cdiario=float(input("Digite o valor do consumo médio diário(litros/dia)= "))

cap_total=((altura*largura*comprimento)/1000)
auton_reser=cap_total/cdiario

print("Capacidade do Reservatório: ",cap_total, "litros: ")

print("Autonomia do reservatório: ",auton_reser,"dias") 

print("\nAgora, vamos classificar o consumo:")

if(auton_reser<2):
        print("\nConsumo Baixo")
      
elif(auton_reser >=2 and auton_reser<7):

     print("\nConsumo Moderado")
else:
      (auton_reser>7)
      print("\nConsumo Alto")