programa {
  funcao inicio() {

    inteiro opcao
 
inteiro senha,conta, agencia,sen,cont,agen,sal,salatual,saque,dep

cadeia cliente=("João")


enquanto (opcao!=5){
escreva("\n       =====================================")
escreva("\n       BANCO PYTHON - SISTEMA BANCÁRIO")
escreva("\n       =====================================")
escreva("\n       Bem - vindo ao terminal de atendimento ")
escreva("\n       =====================================")


escreva ("\nMenu de Opções:")
escreva("\n 1- Cadastro \n2- Saldo \n 3- Saque \n 4- Depósito \n 5- Sair ")
escreva("\nEscolha uma opção:")
leia(opcao)
se(opcao==1){

escreva("\nDigite sua agência:")
leia(agen)
escreva("\nDigite sua conta:")
leia(cont)

escreva("\nDigite sua senha:")
leia(sen)

escreva("\n Saldo inicial:")
leia(sal)
}

senao se (opcao==2) {
  escreva("\nNome do cliente:",cliente)
  escreva ("\nAgência:",agen)
escreva("\nSaldo atual:",sal)
}


senao se (opcao==3){
  escreva("\nQual o valor para saque:",saque)

  leia(saque)
escreva ("\nSaque efetuado")

  se (sal<saque){
  escreva("\nSaldo insuficiente")}

  senao  {
sal=sal-saque
  }
}


senao se (opcao==4){
  escreva("\nQual o valor a ser depósitado:")
  leia(dep)

  sal=sal+dep
escreva("Depósito efetuado")
}


senao se(opcao==5){
  escreva("\nServiço finalizado.")
}
    
}

}
}
