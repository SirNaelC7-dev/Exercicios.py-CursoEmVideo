num=str(input('Digite um número entre 0-9999\n'))
u=num[len(num)-1:len(num)]
d=num[len(num)-2:len(num)-1]
c=num[len(num)-3:len(num)-2]
um=num[-4:-3]
print('Qtd. Unidades: {}\nQtd. Dezenas: {}\nQtd. Centenas: {}\nQtd. Unidade de Milhar: {}'.format(u, d, c, um))

