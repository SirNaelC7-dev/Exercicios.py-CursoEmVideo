nums= ('Zero', 'Um', 'Dois', 'Três', 
       'Quatro', 'Cinco', 'Seis', 'Sete', 
       'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 
       'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 
       'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
	ext=int(input('Digite um número entre 0-20: '))
	if 0<= ext <=20:
		break
	print('Número fora da faixa, Tente novamente')
print(f'Você digitou o número {nums[ext]}')
