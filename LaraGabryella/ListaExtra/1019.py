# https://www.beecrowd.com.br/judge/en/problems/view/1019

tempo = int(input())

hora = tempo // 60**2
temp = tempo - hora * 60**2
minutos = tempo // 60

temp = tempo - minutos * 60

segundos = tempo

print("%i:%i:%i" %(hora, minutos, segundos))
