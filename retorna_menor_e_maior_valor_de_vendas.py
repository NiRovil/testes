"""
Você está trabalhando para uma empresa que fornece materiais escolares e precisa da sua ajuda para entrar no mundo digital. Como primeira atividade, você identificou que não existe uma funcionalidade que é muito importante para a empresa ter mais controle sobre os valores dos produtos vendidos. Esta funcionalidade consiste em descobrir o maior e o menor valor dos produtos vendidos em um período de tempo, para cada vendedor.

Os valores das vendas que devem ser consideradas podem variar entre 20 e 500 reais e estão agrupados por vendedores. Além disso, deve-se ignorar as devoluções, que estão indicadas com o valor 0.

A sua função/método deverá receber uma lista vendas agrupadas por vendedores, (e.g. [[200, 100], [300]]) e retornar um array onde a primeira posição contém o menor valor e a segunda posição o maior valor (e.g. [100, 300]).

Mas preste atenção! Algum vendedor pode não ter realizado vendas no período.
"""

def retorna_menor_e_maior_valor_de_vendas(tickets):
    vendas = []
    resultado = []
    
    #loop para verificar se houve vendas, e se as vendas estão dentro da regra de negócio
    #entre 20 e 500 reais. Se a afirmação for verdadeira o valor é anexado na lista vendas.
    for ticket in tickets:
        if len(ticket) != '':
            for tick in ticket:
                if tick >= 20 and tick <= 500:
                    vendas.append(tick)
    
    #se houver vendas, filtra o valor minimo e o máximo e anexa na lista resultado.
    if vendas:
        minimo = min(vendas)
        maximo = max(vendas)
        
        resultado.append(minimo)
        resultado.append(maximo)
        
    return resultado