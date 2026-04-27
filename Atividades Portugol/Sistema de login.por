programa {
  funcao inicio() {
  inteiro usuario, senha, opcao,alterarsen,mosdadosusuario,logout, sairsis
  inteiro tentativa
enquanto (opcao!=4 ){





  escreva ("\n Sistema de login")
  escreva("\nDigite seu usuário:")
  leia(usuario)
  escreva("\nDigite sua senha:")
  leia(senha)

  se (senha ou usuario){
    escreva("Senha incorreta \nrestam 2 tentativas")
    escreva ("Senha ou usuário errado \n restam 1 tentativa")
    escreva("Senha não correspondente \nACESSO BLOQUEADO")
  }
senao {
  escreva("\nDados ")
  escreva("\nUsuário: ",usuario)

  escreva("\nSenha: ",senha)

}

escreva("\nOpções: \n 1- Alterar senha \n 2- Mostrar dados do usuário \n 3- Fazer logout \n 4- Sair do sistema \n Escolha uma opção:")
leia(opcao)

se(opcao==logout){
  escreva ("Tela de login")
   escreva("\nDigite seu usuário:")
  leia(usuario)
  escreva("\nDigite sua senha:")
  leia(senha)
}

senao se(opcao==alterarsen){
  escreva ("Digite a senha atual para permitir a redefinição")
  leia(senha)
  se(senha==senha){
    escreva("A senha não pode ser igual a antiga")
  }
}

























































}

    
  }
}
