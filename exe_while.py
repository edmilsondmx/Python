inicial = 1000
juros = 0.5
deposito = 50
meses = 0
meta = 10000

#print('Qual o valor inicial?')
#inicial = input()
#print('Qual o objetivo a ser atingido?')
#meta = input()

fator = 1 + (juros / 100)
res = inicial

while res <= meta:
    meses += 1
    res *= fator #aplica juros
    res += deposito #aplica depósito

anos = meses // 12
M = meses % 12


print('Para atingir o objetivo terá que guardar por ',anos,'anos e',M,'meses!')