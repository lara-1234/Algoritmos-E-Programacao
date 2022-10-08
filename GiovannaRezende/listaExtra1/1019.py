#https://www.beecrowd.com.br/judge/pt/problems/view/1019


temp = int(input())


tHora = temp // 60**2

temp = temp - tHora * 60**2

tMin = temp // 60

temp = temp - tMin * 60

tSeg = temp

print("%i:%i:%i" %(tHora, tMin, tSeg))