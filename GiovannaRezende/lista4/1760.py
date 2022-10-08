#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760


cont = 0
soma = 0
qt = 1

while cont <= 3:
  idade = int(input())
  peso = float(input())
  cont = cont + 1
  soma = soma + idade

while peso > 90:
  qt = qt + 1
print("Qtd pessoas > 90Kg: %i" %(qt))

media = soma / 4
print("Idade média: %.2f" %(media))