n = int(input())
cont1 = 0
cont2= 1
while cont1 < n:
    cont2 += cont1
    cont1 += cont2
    print(cont2)
    print(cont1)

    
if cont2 == n or cont1 ==n:
    print (f' {n} é um valor fibonacci')

else:
    print (f' {n} não é um valor fibonacci')
    
   
