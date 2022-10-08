#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714


preco = float(input())

if preco < 20.00:
  valor = (preco * (0.45))
  lucro = (preco + valor)
else:
  valor = (preco * (0.30))
  lucro = (preco + valor)

print("Valor de venda: R$%.2f" %(lucro))