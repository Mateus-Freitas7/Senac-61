programa {
  funcao inicio() {
    cadeia opcoes=("\n1-Adiçao\n2-Subtração\n3-Multiplicação\n4-Divisão\n0- Sair")
cadeia opcao=("Escolha uma opção")
cadeia adicao
cadeia subtracao
cadeia multiplicacao
cadeia divisao
cadeia sair
  real n1adi
  real n2adi
  real n1sub
  real n2sub
  real n1mult
  real n2mult
  real n1div
  real n2div

escreva ("Menu de opções:",opcoes)
escreva("\nEscolha uma opcão:")

enquanto(opcao==adicao){
  escreva("Adição:")

  escreva("\nDigite o primeiro valor:")
leia(n1adi)

escreva("\nDigite o segundo valor:")
leia(n2adi)

escreva("\nA Soma  dos valores é:")
adicao=n1adi+n2adi}



enquanto(opcao==subtracao){
escreva ("Digite o primeiro valor")
leia(n1sub)

escreva("Digite o segundo valor:")
leia(n2sub)

escreva("A Subtração dos valores é:",n1sub-n2sub)
 }

enquanto(opcao==multiplicacao){
  escreva ("Digite o primerio valor:")
  leia(n1mult)

  escreva("Digite o segundo valor:")
  leia(n2mult)

  escreva("A multiplicação dos valores é de: ",n1mult*n2mult)
}
  



  enquanto(opcao==divisao){
    escreva("Digite o primeiro valor:")
    leia(n1div)

    escreva("Digite o segundo valor:")
    leia(n2div)

    escreva("O Valor da divisão é",n1div/n2div)
  }

  

  }
}








}



  }
}
