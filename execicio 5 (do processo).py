palavra = input('palavra:')
tamanho = len(palavra)
i=0
inverta =[]

while tamanho >= 1:
    tamanho -= 1
    i -= 1
    inverta.append(palavra[i])
    

print (f'{ "". join(inverta)}' )
    
    
    
    
    
    
