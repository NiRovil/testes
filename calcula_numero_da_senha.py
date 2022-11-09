"""
Durante uma expedição tecnológica, sua equipe encontrou o que parece ser a senha que lhes dá acesso a um grande tesouro digital. Por sorte, sua equipe é formada pelas pessoas mais feras em programação e vocês rapidamente descobriram como decifrá-la.

Com a possibilidade de que vocês encontrem mais códigos contendo outras senhas, você foi designado à tarefa de desenvolver um algoritmo que decifra os códigos para não precisarem fazer isso de forma manual.

A senha é representada por um número binário de 10 dígitos formado pelo dígito predominante de cada coluna. Caso a coluna tenha a mesma quantidade de dígitos 0 e 1, deve se considerar o número 1.

Exemplo: A primeira coluna da lista tem como dígito predominante o número 1, sendo assim, o primeiro dígito - dos 10 - da senha é 1.

0110100000
1001011111
1110001010
0111010101
0011100110
1010011001
1101100100
1011010100
1001100111
1000011000

Desenvolva um algoritmo que receba um array de valores binários (como o exemplo acima) e retorne a representação decimal da senha.
"""

from statistics import mode

def calcula_numero_da_senha(senha):
  
    index = 0
    senhas = []
    resultado = []
    
    #anexa a lista senhas, ordenadamente todos os numeros do index 1 até n
    while index <= 9:
        for items in senha:
            for item in items[index]:
                senhas.append(int(item))
        index += 1
    
    #divide a lista senhas em uma lista result de tamanho 10
    result = [senhas[item:item + 10] for item in range(0, len(senhas), 10)]
    
    #para cada conjunto de senha(item) na lista result, verifica qual numero é o mais presente.
    #é anexado o numero com a maior moda entre 0 e 1, se a moda entre ambos os números for igual,
    #1 será anexado ao resultado.
    for item in result:
        if item.count(0) == 5:
            resultado.append(1)
        else:
            moda = mode(item)
            resultado.append(moda)

    #agrupa todos os números resultantes.
    agrupador = ''.join(map(str, resultado))
    #converte os numeros agrupados em um decimal.
    resposta = int(agrupador, base=2)

    return resposta