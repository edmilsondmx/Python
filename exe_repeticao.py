inicial = 1000
juros = 0.5
deposito = 50
inflacao = 0.2
anos = 10

fator = 1 + (juros / 100)
fator_inf = 1 + (inflacao / 100)
res = inicial

for i in range(anos * 12):
    res *= fator #aplica juros
    res /= fator_inf #aplica inflação
    res += deposito #aplica depósito


print(res)