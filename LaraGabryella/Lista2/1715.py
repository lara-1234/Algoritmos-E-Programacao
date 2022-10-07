# https://www.beecrowd.com.br/judge/en/custom-problems/view/1715
cliente = int(input())
vl = float(input())

if cliente == 1:
    vl = vl
    print("Valor total a ser pago: R$%.2f" % (vl))
elif cliente == 2: 
    vl = vl - (vl * 0.13)
    print("Valor total a ser pago: R$%.2f" % (vl))
elif cliente == 3:
    vl = vl - (vl * 0.07)
    print("Valor total a ser pago: R$%.2f" % (vl))
else:
    print("OPÇÃO INVÁLIDA!")
