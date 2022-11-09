"""
Um grande amigo seu mora numa cidade pequena, onde existem apenas duas empresas de táxi - a Empresa 1 e a Empresa 2. Ambas mudam suas taxas a cada dia e calculam o valor de suas corridas da seguinte forma: uma taxa fixa mais um valor por quilômetro rodado.
Seu amigo é fisioterapeuta e pega táxis diariamente para visitar seus clientes ao redor da cidade. Você decidiu escrever um código para ajudá-lo a decidir qual empresa escolher para cada uma das corridas, baseado no preço.

Sua função receberá 4 valores: TF1 (a taxa fixa da empresa 1), VQR1 (o valor por quilômetro rodado da empresa 1), TF2 (a taxa fixa da empresa 2), VQR2 (o valor por quilômetro rodado da empresa 2), todos em formato string. Seu retorno deve ser uma string em uma das seguintes formas:

    “Tanto faz” - para o caso de o valor das duas empresas para qualquer corrida ser igual
    “Empresa 1” - se o valor da Empresa 1 for sempre menor que o da Empresa 2
    “Empresa 2” - para o caso contrário do citado acima
    “Empresa Xpto quando a distância < N, Tanto faz quando a distância = N, Empresa Ypto quando a distância > N” para o caso de a escolha depender da distância a ser percorrida (onde Xpto e Ypto representa 1 ou 2 e N representa a distância).

Exemplo:
TF1 = 2,50
VQR1 = 1,00
TF2 = 5,00
VQR2 = 0,75
Output:
“Empresa 1 quando a distância < 10.0, Tanto faz quando a distância = 10.0, Empresa 2 quando a distância > 10.0”
"""

def escolhe_taxi(tf1,vqr1,tf2,vqr2):

    tarifa_empresa_1 = float(tf1)
    valor_rodado_empresa_1 = float(vqr1)
    tarifa_empresa_2 = float(tf2)
    valor_rodado_empresa_2 = float(vqr2)

    distancia = 1
    
    valor_por_km_emp_1 = []
    valor_por_km_emp_2 = []

    #setando uma distancia máxima para efeito de comparação.
    while distancia <= 30:
        valor_cobrado_emp_1 = (valor_rodado_empresa_1 * distancia) + tarifa_empresa_1          
        valor_por_km_emp_1.append(valor_cobrado_emp_1)
        valor_cobrado_emp_2 = (valor_rodado_empresa_2 * distancia) + tarifa_empresa_2
        valor_por_km_emp_2.append(valor_cobrado_emp_2)
        distancia += 1

    valores_por_km = dict(zip(valor_por_km_emp_1, valor_por_km_emp_2))

    #define o valor e a km's em que há um ponto médio entre as duas empresas
    ponto_medio = {valor1: index+1 for index, (key, value) in enumerate(valores_por_km.items()) if key == value for valor1, valor2 in valores_por_km.items() if valor1 == valor2}

    #indexa os valores das corridas, independente do trajeto.
    empresa_1 = [valor_emp_1 for valor_emp_1, valor_emp_2 in valores_por_km.items() if valor_emp_1 < valor_emp_2]
    empresa_2 = [valor_emp_2 for valor_emp_1, valor_emp_2 in valores_por_km.items() if valor_emp_1 > valor_emp_2]

    #se houver um ponto médio, retorna qual a melhor empresa para se pagar pelo táxi.
    if len(ponto_medio) == 1 and empresa_1 and empresa_2:
        output = str.join("", [str(float(valor)) for valor in ponto_medio.values()])
        if sum(empresa_1) < sum(empresa_2):
            return f"Empresa 1 quando a distância < {output}, Tanto faz quando a distância = {output}, Empresa 2 quando a distância > {output}"
        if sum(empresa_1) > sum(empresa_2):
            return f"Empresa 2 quando a distância < {output}, Tanto faz quando a distância = {output}, Empresa 1 quando a distância > {output}"
    
    if empresa_1:
        return "Empresa 1"
    
    if empresa_2:
        return "Empresa 2"
    
    return "Tanto faz"