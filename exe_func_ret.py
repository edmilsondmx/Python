def dolar(valor, cotacao):
    return float(valor) / cotacao


print('Digite o valor do aluguel:')
aluguel = float(input())
print('Digite o valor da contas:')
contas = float(input())
print('Digite o valor do supermercado:')
supermercado = float(input())

cotacao = 5.44

a = dolar(aluguel, cotacao) * 12
c = dolar(contas, cotacao) * 12
s = dolar(supermercado, cotacao) * 12
tot = a + c + s

print('O gasto anual com aluguel é:' + str(a))
print('O gasto anual com contas é:' + str(c))
print('O gasto anual com supermercado é:' + str(s))
print('O gasto anual total é: ' + str(tot))