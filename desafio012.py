saldo=float(input('Digite a quantia na sua carteira: '))
preço=float(input('Qual o preço atual do dólar? '))
conversao=saldo/preço
print('Você pode comprar{:3f} com seu saldo'.format(conversao))
