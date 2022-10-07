# https://www.beecrowd.com.br/judge/en/custom-problems/view/1761

VProduto = 1
To = 0


while VProduto != 0:
  VProduto = float(input())
  if VProduto != 0:
    To = To + VProduto
  
pago = float(input())

TR = pago - To

print("Total da compra: R$%.2f" %(To))
print("Valor pago: R$%.2f" %(pago))
print("Troco: R$%.2f" %(TR))
