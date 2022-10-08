# https://www.beecrowd.com.br/judge/en/problems/view/1017

TempoDeViagem = int(input())
VelocidadeMedia = int(input())

kmL = 12 

qtdLitros = (TempoDeViagem * VelocidadeMedia) / kmL

print("%.3f" %(qtdLitros))
