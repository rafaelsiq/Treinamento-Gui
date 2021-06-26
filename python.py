## definicao de variaveis
## tipo 
## K = 3/4
## pi = 3.14
## r = 10

## funcao K * pi * r*r

k = 3/4
pi = 3.14
r = 0

while(r <= 20): ## enquanto r < 20
    if(r >= 10): ## se o raio for menor que 10
        area = k * pi * r
        print(r, " a area da esfera é: " , area)
    else:
        print(r, " o raio é muito pequeno para eu calcular")
    r = r + 1



