# https://www.beecrowd.com.br/judge/en/custom-problems/view/1759

AnoAtual = int(input())

S = 1000
P = 0.015 

if AnoAtual < 2006:
  print("O ano informado deverá ser > 2005!")
else:
  SF = S + (P * S)

  for x in range (2007,AnoAtual + 1):
    P = P +0.01
    SF = SF + (P * SF)
  print("Salário atual: R$%.2f" %(SF))
