produto = []
qtde = []
preco = []
tot = 0.0

while True:
    print('Digite o nome do produto:')
    prod = input()
    
    if prod == '':
        break

    print('Qual a quantidade?')
    quantidade = int(input()) 
    
    print('Qual o preço?')
    pre = float(input())
    

    produto.append(prod)
    qtde.append(quantidade)
    preco.append(pre)

for i in range(len(produto)):
    print('produto: ' + produto[i].upper() + ',\tquantidade: ' + str(qtde[i]) + '\n')

for i in range(len(produto)):
    res = qtde[i] * preco[i]
    tot += res 

print('Total: ' + str(tot))