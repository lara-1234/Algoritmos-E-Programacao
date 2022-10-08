# https://www.beecrowd.com.br/judge/en/problems/view/1065

NumerosPares = 0

for n in range(5): 
  Numero = int(input())
  if (Numero%2 == 0):
    NumerosPares +=1

print (NumerosPares,"valores pares")
