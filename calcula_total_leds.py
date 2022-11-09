"""
Uma empresa fabrica painéis de LED compostos por quadrados de 1 cm de lado. Nos vértices de cada quadrado fica um LED, 
sendo que o tamanho de cada painel é escolhido pelo cliente conforme a sua necessidade. 
A imagem abaixo mostra um painel de 2 cm por 4 cm, composto por 15 LEDs no total.

Atualmente os funcionários desta fábrica perdem muito tempo (que poderia ser utilizado para inovação) com o cálculo manual desses painéis.
A alta diretoria da fábrica decidiu então contratar você para evoluir e construir um cálculo automatizado, modernizando assim os sistemas deles.

Considerando um painel de n por m centímetros, desenvolva um código para calcular o número total de LEDs no painel.

OBS:

    Os valores da altura e da largura devem ser recebidos por meio de parâmetros

"""

def calcula_total_leds(altura,largura):  
    return 0 if altura == 0 or largura == 0 else (altura+1) * (largura+1) #retorna o resultado da condicional.