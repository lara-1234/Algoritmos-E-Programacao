# https://www.beecrowd.com.br/judge/en/custom-problems/view/1713

vh = float(input())

ht = float(input())




sl = vh * ht

imp = (sl * (0.11))

inss = (sl * (0.08))

sind = (sl * (0.05))



liquido = ((sl) - (imp) - (inss) - (sind))



print("Salário bruto: R$%.2f" %(sl))

print("Imposto: R$%.2f" %(imp))

print("INSS: R$%.2f" %(inss))

print("Sindicato: R$%.2f" %(sind))

print("Líquido: R$%.2f" %(liquido))