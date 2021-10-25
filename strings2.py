# concatenação

x = 10
print('x vale: '+ str(x) + ' minutos')

# indexando
# slices

texto = "Item: Carro"
#indice  012345678910
print(texto[10])

print(texto[6:11])
print(texto[6:])

# lower(), upper()

texto = 'Olá Mundo'
print(texto.lower())
print(texto.upper())

# in
texto = 'Olá mundo!'

if 'olá' in texto.lower():
    print('o texto tem um olá')