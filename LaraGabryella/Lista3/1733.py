# https://www.beecrowd.com.br/judge/en/custom-problems/view/1733
Nome = (input())
Horas = float(input())

ShExtra = (Horas * (10))
Sbruto = ((3) * 1192.40 + ShExtra) 

if Sbruto > 2000.00:
  INSS = (Sbruto * (0.12))
else:
  INSS = (Sbruto * (0.5))
if Sbruto > 2500.00:
  imposto = (Sbruto * (0.20))
else:
  imposto = (Sbruto * (0.0))
Slíquido = (Sbruto - (INSS) - (imposto)) 

print("Nome: %s" %(Nome)) 
print("Salário bruto: R$%.2f" %(Sbruto))
print("Salário líquido: R$%.2f" %(Slíquido))
