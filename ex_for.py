inicial = 1000
juros = 0.5
i = 0
anos= 1
fator = 1 + (juros /100)
res = inicial
for n in range(anos * 12):
    res *= fator
    i += 1
    #print('Após ',i,'meses você terá: ',res)


print('Valor final será:')
print (res)