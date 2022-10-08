#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761


valorProd = 1
total = 0
while valorProd != 0:
  valorProd = float(input())
  if valorProd != 0:
    total = total + valorProd
  
pago = float(input())

troco = pago - total

print("Total da compra: R$%.2f" %(total))
print("Valor pago: R$%.2f" %(pago))
print("Troco: R$%.2f" %(troco))