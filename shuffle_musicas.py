"""
Sua equipe está trabalhando em um app de streaming de músicas e uma das funcionalidades é criar um embaralhador de músicas. 
Uma pesquisa feita pela equipe de UX (experiência do usuário) mostrou que essa é uma das funcionalidades mais importantes 
para os usuários e por isso foi priorizada a criação de um experimento para testar a melhor solução.

A ideia é criar vários embaralhadores diferentes e realizar um teste com partes dos usuários (chamado de teste A/B), 
onde cada grupo de usuários selecionado recebe uma versão e através de pesquisas e métricas de utilização saberemos qual terá a maior aceitação.

Sua tarefa será desenvolver um desses embaralhadores. Você deve criar uma função que receberá uma lista de pesos que 
representa as músicas mais ouvidas pelo usuário. Sua função deve retornar uma lista organizada intercalando as músicas 
mais ouvidas com as músicas menos ouvidas. Por exemplo:

Na situação onde a lista de pesos é: [2, 10, 5, 3] sua função deverá retornar [10, 2, 5, 3]
"""

import itertools

def shuffle_musicas(musicas_tocadas):

    if musicas_tocadas:

        #ordena do menor para o maior e vice versa, salvando em listas distintas.
        menor_maior = sorted(musicas_tocadas, key=int)
        maior_menor = sorted(musicas_tocadas, key=int, reverse=True)

        #intercala os maiores pesos com os menores pesos.
        intercalacao = list(itertools.chain(*zip(maior_menor, menor_maior)))

        #define o separador. como a intercalacao junta as duas listas, é feita a divisão por 2.
        separador = len(intercalacao) / 2

        #divide a lista intercalacao em uma lista resultado com o tamanho definido no separador.
        resultado = [intercalacao[item:item + int(separador)] for item in range(0, len(intercalacao), int(separador))]

        return resultado[0]
    
    return []