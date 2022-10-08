#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713


valorHora = float(input())
horasTrabalhadas = float(input())

salario = valorHora * horasTrabalhadas
imposto = (salario * (0.11))
inss = (salario * (0.08))
sindicato = (salario * (0.05))

liquido = ((salario) - (imposto) - (inss) - (sindicato))

print("Salário bruto: R$%.2f" %(salario))
print("Imposto: R$%.2f" %(imposto))
print("INSS: R$%.2f" %(inss))
print("Sindicato: R$%.2f" %(sindicato))
print("Líquido: R$%.2f" %(liquido))