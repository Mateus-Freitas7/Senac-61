programa {
  funcao inicio() {
    inteiro senha= 1234,conta=1234, agencia=1234,sen,cont,agen
inteiro saldo=1,extrato=2,pagamento=3,saque=4,deposito=5,sair=0,opcao
    cadeia senha=("1234")
    cadeia conta=("1234")
    cadeia agencia=("1234")
cadeia opcao=("Escolha uma opção:")
real sal=1000,ext=100,pag,saq,dep,sair


    escreva ("    =====================================")
escreva("\n       BANCO PYTHON - SISTEMA BANCÁRIO")
escreva("\n       =====================================")
escreva("\n       Bem - vindo ao terminal de atendimento ")
escreva("\n       =====================================")
escreva("\n       Segurança . Rapidez . Confiança")
escreva("\n       =====================================")

escreva("\nDigite sua agência:",agen)
leia(agen)

escreva("\nDigite sua conta:",cont)
leia(cont)

escreva("\nDigite sua senha:",sen)
leia(sen)

se(senha==sen e conta==cont e  agencia==agen){
escreva("\nACESSO PERMITIDO!")
escreva("\n===== MENU DO BANCO=====")
escreva("\n1- Saldo")
escreva("\n2- Extrato")
escreva("\n3- Pagamento")
escreva("\n4- Saque")
escreva("\n5- Depósito")
escreva("\n0- Sair ")
escreva("\nEscolha uma opção: ")
leia(opcao)}

senao{
  escreva("ACESSO NEGADO")
}

se(opcao==saldo){
escreva("Seu saldo é de:",sal)
}

senao{
  se(opcao==extrato)
  escreva("\nRecebeu" ,ext, "de João:")
  escreva("\nSaldo Atual:",sal+ext)

}

  
    se(opcao==pagamento){
  escreva("Valor a ser pago:")
  leia(pag)
  se(pag<=sal)
  escreva("Pagamento aceito")
  }

  se(pag>sal){
    escreva("Pagamento recusado")
    escreva("Saldo Atual:",sal-pag)
  }
  
senao{
  se(opcao==saque)
  escreva("Valor a ser sacado:")
  leia(saq)
escreva("\nSaldo Atual:")
sal-saq
}


  se(opcao==deposito){
  escreva("\nQual valor a ser depósitado:",dep)
  escreva ("Saldo Atual:")
  sal+dep
}



  




  




  }
}
