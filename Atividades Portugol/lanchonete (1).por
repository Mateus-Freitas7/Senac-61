programa {
  funcao inicio() {
  
real quantidade
real sanduiche=12.50, refrigerante=6.80, sobremesa=8.75,pago,s,r,ss,cs,cr,css,qnt,vlr,tr
real dinheiro
escreva("\nQuantidade de Sanduíches|:")
leia(s)

escreva("\nQuantidade de Sobremesas:")
leia (ss)

escreva("\nQuantidade de Refrigerantes:")
leia(r)

escreva("\nValor pago pelo cliente em dinheiro:")
leia(pago)

cs=sanduiche*s

cr=refrigerante*r

css=sobremesa*ss

qnt=s+ss+r

vlr=cr+cs+css

tr=pago-vlr

escreva("\n............EXTRATO............")

escreva("\nQuantidade de Sanduíches:",s)

escreva("\nQuantidade de Sobremesas:",ss)

escreva("\nQuantidade de Refrigerantes:",r)

escreva("\nValor pago pelo cliente em dinheiro:",pago)


escreva("\n............VALOR TOTAL GASTO............")

escreva("\nnValor total gasto em Sanduíches:",cs)

escreva("\nValor total gasto em Sobremesas:",css)

escreva("\nValor total gasto em Refrigerantes:",cr)


escreva("\n............INFORMAÇÕES............")

escreva("\nQuantidade total de itens comprados:",qnt)

escreva("\nValor total do pedido:",vlr)


escreva("\nValor do troco a ser devolvido ao cliente:",tr)







  }
}
