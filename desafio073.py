teams=('Flamengo', 'Internacional', 'Atlético - MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athlétcio - PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético - GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
print('Os 5 primeiros colocados foram:')
for c in range(0,5):
	print(teams[c], end = ' ')
print('')
print('=-=' * 19)	

print('Os 4 últimos colocados foram:')
for c in range(len(teams)-4,len(teams)):
	print(teams[c], end = ' ')
	
print('')
print('=-=' * 19)	
print(sorted(teams))
