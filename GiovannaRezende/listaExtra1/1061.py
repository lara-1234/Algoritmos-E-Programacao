#https://www.beecrowd.com.br/judge/pt/problems/view/1061



Página inicialPYTHONURI PROBLEMA 1061 - Tempo de um Evento SOLUÇÃO EM PYTHON
URI PROBLEMA 1061 - Tempo de um Evento SOLUÇÃO EM PYTHON
Garcia 9/25/2018 05:34:00 PM
URI Online Judge | 1061
Tempo de um Evento
Adaptado por Neilor Tonin, URI  Brasil
Timelimit: 1
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo em segundos que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento..
Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.
Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.
Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.




URI Online Judge | 1061
Event Time
Adapted by Neilor Tonin, URI  Brazil
Timelimit: 1
Peter is organizing an event in his University. The event will be in April month, beginning and finishing within April month. The problem is: Peter wants to calculate the event duration in seconds, knowing obviously the begin and the end time of the event.
You know that the event can take from few seconds to some days, so, you must help Peter to compute the total time corresponding to duration of the event.
Input
The first line of the input contains information about the beginning day of the event in the format: “Dia xx”. The next line contains the start time of the event in the format presented in the sample input. Follow 2 input lines with same format, corresponding to the end of the event.
Output
Your program must print the following output, one information by line, considering that if any information is null for example, the number 0 must be printed in place of W, X, Y or Z:




dia_i = input().split()
hora_i = input().split()
dia_f = input().split()
hora_f = input().split()
di, df = int(dia_i[1]), int(dia_f[1])
hi, mi, si = int(hora_i[0]), int(hora_i[2]), int(hora_i[4])
hf, mf, sf = int(hora_f[0]), int(hora_f[2]), int(hora_f[4])

minuto_seg = 60
hora_seg = minuto_seg * 60
dia_seg = hora_seg * 24
i = si + mi*minuto_seg + hi*hora_seg + di*dia_seg
f = sf + mf*minuto_seg + hf*hora_seg + df*dia_seg
if i < f:
    tempo = f - i
    dias = int(tempo/dia_seg)
    tempo = tempo%dia_seg
    horas = int(tempo/hora_seg)
    tempo = tempo%hora_seg
    minutos = int(tempo/minuto_seg)
    tempo = tempo%minuto_seg
    segundos = tempo
    print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))
