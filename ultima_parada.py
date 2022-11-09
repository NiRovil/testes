"""
Você e seu time estão desenvolvendo um sistema de indicações de postos de gasolina que ficam próximos da localização atual do veículo. No modo de direção “viagem”, a funcionalidade a ser desenvolvida é de indicar ao condutor o posto mais distante possível dentro do limite atual de combustível. E caso não exista posto de gasolina, retornar -1

A pessoa responsável por fazer a especificação do sistema informou que você terá as seguintes informações: consumo médio de combustível, quantidade de combustível restante no veículo e um array contendo distâncias dos postos de gasolinas.

Exemplo:
Combustivel (em litros): 2
Consumo médio (km/l): 8
Postos de Gasolina (km): [2, 15, 22, 10.2]
"""

def ultima_parada(combustivel,consumo,postos_de_gasolina):
    
    kms = combustivel * consumo
    relacao = {}
    resultado = {}
    
    #loop para calcular a média de consumo de combustível máxima que pode ser usada até o posto X
    #quanto mais próximo o valor resultante é de 1, significa que o combustível atual será suficiente
    #até a próxima parada, abaixo de 1 o combustível não é suficiente. Cada posto é anexado em um
    #dicionário com sua kilometragem como chave, e o resultado da média como seu valor.
    for posto in postos_de_gasolina:
      mais_proximo = kms/posto
      relacao[posto] = mais_proximo
    
    #loop para verificar se o combustível será suficiente para chegar ao posto X, anexa todos os valores
    #maiores que 1.
    for chave, valor in relacao.items():
        if valor > 1:
            resultado[chave] = valor
    
    #verifica se há postos perto o suficiente.
    existencia = min(relacao.items())
    if existencia[1] < 1:
        return -1
      
    #retorna o posto mais distante o qual o combustível atual consegue suprir.    
    resposta = min(resultado.items(), key=lambda x: x[1])

    return resposta[0]