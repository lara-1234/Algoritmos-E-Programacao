#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737


num = int(input())

total = float()

if num > 0:
    while num > 0:
        soma = int(input())
        total = total + soma
        num = num - 1
    print("Soma dos números informados: %.2f" %(total))
else:
    print("Informe uma quantidade > 0!")