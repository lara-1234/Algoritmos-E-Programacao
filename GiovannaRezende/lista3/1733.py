#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733


nome = input()
horas = float(input())

salario_hextra = (horas * (10))
salario_bruto = ((3) * 1192.40 + salario_hextra) 

if salario_bruto > 2000:
  inss = (salario_bruto * (0.12))
else:
  inss = (salario_bruto * (0.5))
  
valor = salario_bruto - inss

if valor > 2500:
  imposto = (salario_bruto * (0.20))
else:
  imposto = (salario_bruto * (0))

liquido = (salario_bruto - imposto - inss)

print("Nome: %s" %(nome))
print("Salário Bruto: R$%.2f" %(salario_bruto)) 
print("Salário líquido: R$%.2f" %(liquido))