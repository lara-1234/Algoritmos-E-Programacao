#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715


codigo = int(input())
valorCompra = float(input())

if codigo == 1:
    valorCompra = valorCompra
    print("Valor total a ser pago: R$%.2f" % (valorCompra))
elif codigo == 2:
    valorCompra = valorCompra - (valorCompra * 0.13)
    print("Valor total a ser pago: R$%.2f" % (valorCompra))
elif codigo == 3:
    valorCompra = valorCompra - (valorCompra * 0.07)
    print("Valor total a ser pago: R$%.2f" % (valorCompra))
else:
    print("OPÇÃO INVÁLIDA!")