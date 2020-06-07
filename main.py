print('FATURA INTERNAÇÃO\n')

while True:
	opq = int(input('\n Qual o tipo do quarto utilizado pelo paciente?\n 1. Quarto particular.\n 2. Quarto semi-particular.\n 3. Quarto coletivo.\n 4. Sair\n'))
	if opq == 4:
		print('\nOPERAÇÃO FINALIZADA PELO USUÁRIO.\n')
		break
	if opq == 1:
		diaria = 360
		tipo = '\nQuarto particular.\n'
	elif opq == 2:
		diaria = 210
		tipo = '\nQuarto semi-particular.\n'
	elif opq == 3:
		diaria = 185
		tipo = '\nQuarto coletivo.\n'
	diarias = int(input('\n Quantos dias de internação?\n'))
	internet = int(input('\n Utilizou a internet?\n 1. Sim. \n 2. Não.\n'))
	if internet == 1:
		net = 3
	else:
		net = 0
	tv = int(input('\n Utilizou a TV a cabo?\n 1. Sim \n 2. Não \n'))
	if tv == 1:
		tvc = 4
	else:
		tvc = 0
	
	totaldia = diarias * diaria
	totalnet = net
	totaltv = tvc

	print('\nHospital Comunitário:\n'
	'Dias no hospital:..........', diarias,'\n'
	'Tipo de quarto:..........:',tipo,'\n',
	'Diárias:.........R$%.2f'%totaldia,'\n',
	'Internet:..........R$%.2f'%net,'\n',
	'TV a Cabo:..........R$%.2f'%tvc,'\n'
	'\nTotal:..........R$%.2f'%(totaldia+totalnet+totaltv),'\n')


