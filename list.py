#lista vazia
lista_vazia = []
print(lista_vazia)

#criar uma list
lista = [1, 2.5, True, 'abc', False]
lista[3] = 'cba'
print(lista)

#len / tamanho da lista
l = [1, 5, 10]
tamanho = len(l)
print(tamanho)
print(len(l))

# indexar list
l = [1, 5, 10, 20]
#    0  1  2   3      

for i in range(len(l)):
    print('elemento indice')
    print(i)
    print('Valor:')
    print(l[i])
    print('')

# criar list com range
l = list(range(10))
print(l)
 