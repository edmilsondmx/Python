#inteiros
x = 10
print(type(x))
y = -1
print(type(y))

#float
x = 3.14
print(type(x))
y = -1.0
print(type(y))

#string
x = 'la la la'
print(type(x))
y = '3'
print(type(y))

#bool
x = True
print(type(x))
y = False
print(type(y))

if x:
    print('x é verdadeiro')
else:
    print('x é falso')
if y:
    print('y é verdadeiro')
else:
    print('y é falso')


#print('Qual o seu sálario?')
salario = 10000


if salario > 20000:
    rico = True
else:
    rico = False
if rico:
    print('Parabéns, você adquiriu nosso cartão de crédito plus!')
else:
    print('Lamentamos, infelizmente não podemos te oferecer o cartão plus!')