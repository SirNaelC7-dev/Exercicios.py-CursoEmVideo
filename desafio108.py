import moedafor
p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedafor.moedafor(p)} é {moedafor.moedafor(moedafor.metade(p))}')
print(f'O dobro de {moedafor.moedafor(p)} é {moedafor.moedafor(moedafor.dobro(p))}')
print(f'Aumentando 30% temos {moedafor.moedafor(moedafor.aumentar(p, 30))}')

