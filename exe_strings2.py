produto = []

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
    

    produto.append(prod, quantidade, pre)

    tot += quantidade * pre
    

for i in range(len(produto)):
    print('produto: ' + produto[i][0].upper() + ', quantidade: ' + str(produto[i][2]))



print('Total: ' + str(tot))