lista = []

while True:
    print('Digite uma cor:')
    entrada = input()
    if entrada in lista:
        print('Esta cor já esta na lista')
    else:
        lista.append(entrada)
    if entrada == '':
        break

lista.sort()
print('Lista de cores:')
print(lista)