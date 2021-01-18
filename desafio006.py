#1-(); 2:**; 3:*, /, //, %; 4:+, -.
#alinhamento no format: <>^
n1=int(input('digite um número: '))
n2=int(input('Digite outro número: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
p=n1**n2
print('A soma é: {}, o produto é: {}, e a divissão é:{:3f}'.format(s,m,d))
print('Divisão inteira é: {} e potência: {}'.format(di,p))
