programa {
  funcao inicio() {
  inteiro  senha, opcao=0,senha_correta=1234,sair,x,senhanova,senha_correta3,usuario3,sen,usua
  inteiro senha_digitada2
  inteiro tentativa=3
  cadeia usuario="Admin"
  cadeia usuario2="Admin"
  inteiro senha_correta2=1234
  inteiro senha_digitada=1234
  
enquanto (opcao!=4 ){


  escreva ("\n Sistema de login")
  escreva("\nDigite seu usuário:")
  leia(usuario2)
  escreva("\nDigite sua senha:")
  leia(senha_digitada2)


  se (senha_digitada2==senha_digitada e usuario2==usuario){

    escreva("\nOpções: \n 1- Alterar senha \n 2- Mostrar dados do usuário \n 3- Fazer logout \n 4- Sair do sistema \n Escolha uma opção:")
    leia(opcao)

 se(opcao==1){
  escreva ("\nDigite a senha atual para permitir a redefinição: ")
  leia(senha)

  se(senha_digitada==senha){
      escreva("Digite uma nova senha:")
      leia(senhanova)
      se (senhanova!=senha_digitada){
      senha_digitada=senhanova
      escreva("\n Senha redefinida")
      }
      senao{
      escreva("As senhas não podem ser iguais")  
      }
    }
  senao{
      escreva("A senha não pode ser igual a antiga")
    }
  }


    senao se (opcao==2){
      escreva("\nDados do Usuário: \n Usuário:",usuario,"\nSenha:",senha_digitada)
 }
    se(opcao==3){
      escreva ("Logout")
      pare
    }

}

senao{
  tentativa=tentativa-1
  escreva("senha ou usuário incorretos - restam, " ,tentativa, "tentativas ")
  se (tentativa==0){
    pare
  }
}





}








}}


























































}

    
  }
}
