#https://www.beecrowd.com.br/judge/pt/problems/view/1065


cont = 0
for x in range(5):
  n = int(input())
  if n%2 == 0:
    cont = cont + 1
print("%i valores pares" %(cont))