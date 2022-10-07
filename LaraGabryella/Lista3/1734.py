# https://www.beecrowd.com.br/judge/en/custom-problems/view/1734
Numero = int(input())

R = 1
count = 1

while count <= Numero:
  R = R * count
  count = count + 1 
  
print("%i!" %(Numero), "= %i"%(R))
