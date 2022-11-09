"""
Dizemos que um número natural X esconde o Y quando, ao apagar alguns algarismos de X, o número Y aparece. Por exemplo, o número 12345 esconde o número 235, uma vez que pode ser obtido ao apagar os números 1 e 4. Por outro lado, ele não esconde o número 154.

A imagem demonstra números: 1,2,3,4,5 todos estão em azul, mas o número 1 e 4 estão com um risco vermelho.

Escreva um código que recebe dois números e que retorna um booleano dizendo se o primeiro esconde o segundo.
"""

def checa_numero_escondido(numero,numero_oculto):
  
    #faz um primeiro check, se o tamanho do primeiro numero (em caracteres) for 
    #menor que o segundo, já há o descarte dos demais testes. Por exemplo: 25/625
    if len(str(numero)) < len(str(numero_oculto)):
        return False
    
    #converte os numeros em string, para acesso de cada numero individualmente.
    converte_numero = str(numero)
    converte_numero_oculto = str(numero_oculto)

    ocultos = []
    
    for num in range(len(converte_numero)):
        for num_oculto in range(len(converte_numero_oculto)):
            #para cada número em converte_numero, verifica se há correspondência.
            #se houver anexa aos números que serão ocultados.
            if converte_numero[num] == converte_numero_oculto[num_oculto]:
                ocultos.append(converte_numero[num])

    if ocultos:
        return True

    return False