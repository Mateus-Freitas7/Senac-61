programa {
  funcao inicio() {

real n1
real n2
real n3
real n4
real media
real soma
cadeia nome=("Maurício")
cadeia sexo=("Masculino")
cadeia endereco=("Rua América")
cadeia telefone=("(67)9944-7788")
cadeia cidade=("Campo Grande")
cadeia estado=("MS")
cadeia pais=("Brasil")
cadeia pai=("Marcos")
cadeia filhos=("4")
cadeia mae=("Marcela")
cadeia idade=("30")


escreva ("\nDigite o seu nome = ",nome)
leia (nome)

escreva ("\nDigite o seu sexo = ")
leia (sexo)

escreva ("\nDigite o seu Endereço = ")
leia (endereco)

escreva ("\nDigite o seu Telefone = ")
leia (telefone)

escreva ("\nDigite o sua Cidade = ")
leia (cidade)

escreva ("\nDigite o seu Estado = ")
leia (estado)

escreva ("\nDigite o seu País = ")
leia (pais)

escreva ("\nDigite o nome do seu Pai = ")
leia (pai)

escreva ("\nDigite o nome da sua Mãe = ")
leia (mae)

escreva ("\nDigite a sua Idade = ")
leia (idade)

escreva ("\nDigite o numero de filhos = ")
leia (filhos)

escreva ("\nDigite a nota 1 = ")
leia (n1)

escreva ("\nDigite a nota 2 = ")
leia (n2)

escreva ("\nDigite a nota 3 = ")
leia (n3)

escreva ("\nDigite a nota 4 = ")
leia (n4)

escreva("Olá sr:",nome,"Idade:",idade,"Telefone:",telefone,"Situado no endereço:",endereco,"Cidade:",cidade,"Estado:",estado,"País:",pais,"Filho de Pai e Mãe:",pai, mae,"Atualmante com:",filhos)

soma=n1+n2+n3+n4
escreva("Total:",n1+n2+n3+n4 )
media=soma/4
escreva(" Possui média  = " ,media)


  }
}
