#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734


n = int(input())

result = 1
count = 1

while count <= n:
  result*=count
  count += 1
print("%i!" %(n),"= %i"%(result))