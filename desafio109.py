import moedaform
p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedaform.moedaform(p)} é {moedaform.metade(p, True)}')
print(f'O dobro de {moedaform.moedaform(p)} é {moedaform.dobro(p, True)}')
print(f'Aumentando 30% temos {moedaform.aumentar(p, 30, True)}')
print(f'Reduzindo 25% temos {moedaform.diminuir(p, 25, True)}')
