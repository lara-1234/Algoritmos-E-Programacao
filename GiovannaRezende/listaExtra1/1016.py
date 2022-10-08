#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716


plano = input()
atsalario = float(input())

if plano == "A":
  novosalario = (atsalario + (atsalario * 0.10))
elif plano == "B":
  novosalario = (atsalario + (atsalario * 0.15))
elif plano == "C":
  novosalario = (atsalario + (atsalario * 0.20))

print("Novo salário: R$%.2f" %(novosalario))