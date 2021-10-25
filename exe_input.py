#inicial = 1000
#juros = 0.5
#deposito = 50
#meta = 10000

print('Qual o valor inicial?')
inicial = float(input())
print('Qual o depósito mensal?')
deposito = float(input())
print('Qual o objetivo a ser atingido?')
meta = int(input())
print('Qual a taxa de juros?')
juros = float(input())

fator = 1 + (juros / 100)
res = inicial

meses = 0

while True:
    meses += 1
    res *= fator #aplica juros
    res += deposito #aplica depósito

    if res >= meta:
        break

anos = meses // 12
M = meses % 12

print(res)
print('Para atingir o objetivo terá que guardar por ',anos,'anos e',M,'meses!')