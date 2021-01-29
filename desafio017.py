import math
co=int(input('Digite o comprimento do cateto oposto: '))
ca=int(input('Digite o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa é: {:.3f}'.format(math.sqrt((math.pow(co,2)+math.pow(ca,2)))))
