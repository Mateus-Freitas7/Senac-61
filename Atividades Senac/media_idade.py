alunos = []
nota_1 = []
nota_2 = []




while True:
     try:
        opcao = int (input("1 - Cadastrar alunos \n2 - Listar alunos cadastrados \n3 - Consultar situação do aluno \nEscolha uma opção:"))
        break
     except:
          print("Apenas opções disponíveis no menu!")

match opcao:
     case 1:
        quantidade  = int (input("Quantidade de alunos que serão cadastrados:"))
        for i in range (quantidade):
            print("Cadastro de alunos!")
            nome = (input("Nome do aluno:"))
            alunos.append(nome)
            while True:
                 try:
                    n1 = float (input("Nota 1:")) 
                    break
                 except:
                      print("Apenas números!")
                      if n1 > 10:
                       print("Apenas de 0 a 10!")
                      else:
                       nota_2.append(n2)

            while True:
                try:
                    n2 = float (input("Nota 2:"))
                    break
                except:
                    print("Apenas números!")
            if n2 > 10:
                        print("Apenas de 0 a 10!")
            else:
                nota_2.append(n2)

            print("Cadastro realizado!")
        
        
     case 2:
        print("Listar alunos!")
        for i in alunos:
             print(i)
     case 3:
        print("Consultar situação do aluno!")
        consulta = (input("Nome para consulta:"))
        if consulta in alunos:
            indice = alunos.index(consulta)
            media = nota_1[indice] + nota_2[indice] /2
            print("Média:",media)




