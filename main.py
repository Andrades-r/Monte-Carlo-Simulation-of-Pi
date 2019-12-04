import random as rd

cnt= 0
n = 10000
for i in range (n):
    x = rd.random()
    y = rd.random()
    if x**2 + y**2 <1:    #Se o ponto (x,y) esta dentro da circunferencia
        cnt +=1
razao = float(cnt)/float(n)
pi = 4.0*razao
print("%.5f" %pi)