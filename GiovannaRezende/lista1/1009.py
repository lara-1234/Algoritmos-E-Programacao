#https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = input()
salarioFixo = float(input())
vendas = float(input())

salarioFinal = salarioFixo + ((vendas / 100) * 15)

print("TOTAL = R$ %.2f" %(salarioFinal))