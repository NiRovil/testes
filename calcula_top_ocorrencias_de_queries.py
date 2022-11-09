"""
Dada um texto qualquer e um lista de termos de pesquisa (sequencia de caracteres), retorne os primeiros K termos mais recorrentes na string, onde K é um parâmetro configurável.

Exemplo:

String: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"

Lista de termos: ["a", "em", "i", "el"]

K: 2

Resultado: ["i", "a"]

Explicação:

Ocorrências de cada termo,"i": 11, "a": 7, "em": 2, "el": 1, com K = 2, retornamos "i" e "a" ordenados conforme a quantidade de ocorrências de cada termo.

Obs: Quando houver termos com quantidades iguais, priorizar o retorno de acordo com a ordem de ocorrência do termo na string.
"""

def calcula_top_ocorrencias_de_queries(texto,queries,k):

    count = 0
    dicionario = {}
    resultado = []
    
    #passa pelos caracteres da querie e soma a quantidade que esses aparecem, indexando 
    #como chave/valor no dicionário
    for caracter in queries:
        contador = texto.lower().count(caracter)
        dicionario[caracter] = contador
        
    #ordena o dicionário com base no caracter que mais aparece
    dicionario_ordenado = {chave: valor for chave, valor in sorted(dicionario.items(), key=lambda item: -item[1])} 

    #loop para mostrar somente a quantidade setada pela váriavel k
    for key, value in dicionario_ordenado.items():
        resultado.append(key)
        count += 1
        if count == k:
            break
            
    return resultado