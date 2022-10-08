#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759


ano = int(input())

salario = 1000
porc = 0.015

if ano < 2006:
  print("O ano informado deverá ser > 2005!")
else:
  sfinal = salario + (porc * salario)
  
  for x in range (2007,ano + 1):
    porc = porc + 0.01
    sfinal = sfinal + (porc * sfinal)
  print("Salário atual: R$%.2f" %(sfinal))