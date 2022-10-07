# https://www.beecrowd.com.br/judge/en/custom-problems/view/1716
plano = input()
SLatual = float(input())

if plano == "A":
  SLnovo = (SLatual + (SLatual * 0.10))
elif plano == "B":
  SLnovo = (SLatual + (SLatual * 0.15))
elif plano == "C":
  SLnovo = (SLatual + (SLatual * 0.20))

print("Novo salário: R$%.2f" %(SLnovo))
