#append()
l = [1, 2, 3]
print(l)
l.append(4)
print(l)
l.append([6, 5, 4])
print(l)
#[1, 2, 3, 4, [6, 5, 4]]
# 0  1  2  3   4
#print(l[4])
#print(l[4][2]) #exibir indice 2 da lista interna 4

# pop()
for i in range(len(l)):
    l.pop()
    print(l)

# remove()

l = ['ana', 'beto', 'carlos']

l.remove(l[1])
print(l)

# sort()

l = ['Maria', 'Adalbeito', 'Carlos', 'Felipe', 'Aurora', 'Tatiane']
print(l)
l.sort()
print(l)
l = [1, 85, 24, 79, 21, 33, 46]
print(l)
l.sort()
print(l)

# in

cores = ['azul', 'Verde', 'Amarelo']
print(l)

print('Digite uma cor:')
#entrada = input()



#if entrada in cores:
    #print('Essa cor já existe')
#else:
    #cores.append(entrada)
#print(cores)

# for

l = [1, 3, 55]

for i in range(len(l)):
    print(l[i])

for i in l:
    print(i)

# slice

lista = list(range(10))
print(lista)