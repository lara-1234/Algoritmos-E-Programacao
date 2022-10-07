# https://www.beecrowd.com.br/judge/en/custom-problems/view/1714

P = float(input())
if P < 20.00:
	VL = (P * (0.45))
	LUC = (P + VL)
else:
	VL = (P * (0.30))
  
	LUC = (P + VL)
print("Valor de venda: R$%.2f" %(LUC))