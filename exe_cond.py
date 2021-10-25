inicial = 1000
juros = 0.5
deposito = 50
anos = 5 
meta = 10000

fator = 1 + (juros / 100)
res = inicial

for i in range(anos * 12):
    res *= fator #aplica juros
    res += deposito #aplica depósito


if res >= meta:
    print('Objetivo foi atingido. Você acumulou: R$', res)
elif res >= (meta * 0.75):
    print('Objetivo não foi atingido, mas quantia chegou a 75% do desejado. Valor: R$', res)
else:
    print('Quantia final é menos de 75% do objetivo. Valor: R$', res)