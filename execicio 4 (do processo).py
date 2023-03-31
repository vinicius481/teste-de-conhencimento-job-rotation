def percentual (valor,total):
    calculo = valor * 100/ total
    return calculo

cont = 0

estados_faturamento ={'SP': 67836.43, 'RJ': 36678.66, 'ES' : 27165.48, 'Outros'  : 19849.53}
total = estados_faturamento ['SP'] + estados_faturamento ['RJ'] + estados_faturamento['ES'] + estados_faturamento['Outros']

for estados,valor in estados_faturamento.items():
    print (f' O estado {estados} participou de aproximadamente {percentual(valor,total):,.2f}% do faturamento deste mes')
    
    




