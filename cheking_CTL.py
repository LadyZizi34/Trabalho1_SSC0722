

def analise(z,parametros,flag,count):

	

		if(z <= len(parametros)):
		  
			# Z é um indice que representa a lista de parâmetros e controla qual está sendo lido
			parametro = parametros[z]

			# Leitura de operadores básicos
			if(parametro == '('):
				z += 1
				count += 1
				analise(z,parametros,flag,count)

			elif(parametro == ')'):
				count -= 1				
				if(flag == 'False'): 
					print ('Entrada mal formada!')
					return False             
			
			elif(parametro == '&'):
			  z += 1
			  analise(z,parametros,flag,count)

			elif(parametro == '|'):
			   z += 1
			   analise(z,parametros,flag,count)

			elif(parametro == '->'):
				z += 1
				analise(z,parametros,flag,count)
			   
			elif(parametro == '<->'):
				z += 1
				analise(z,parametros,flag,count)

			# Leitura de parametros/Operadores CTL
			# Cada operador trata os parametros de forma própria

			elif(parametro == 'AF'):
				z += 2		# passo de 2 para pular o parenteses
				parametro = parametros[z]				
				
				if(parametro == 'p'):
					flag = funcao.af(parametro)
					z += 2
					analise(z,parametros,flag,count)
						
				elif(parametro == 'q'):
					flag = funcao.af(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!p'):
					flag = funcao.af(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!q'):
					flag = funcao.af(parametro)
					z += 2
					analise(z,parametros,flag,count)
				
				else:
					analise(z,parametros,flag,count) # se não é rótulo, então tenho outro operador!

			elif(parametro == 'AG'):
				z += 2
				parametro = parametros[z]
				
				if(parametro == 'p'):
					flag = funcao.ag(parametro)
					z += 2
					return flag
						
				elif(parametro == 'q'):
					flag = funcao.ag(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!p'):
					flag = funcao.ag(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!q'):
					flag = funcao.ag(parametro)
					z += 2
					analise(z,parametros,flag,count)
				
				else:
					analise(z,parametros,flag,count)
			   

			elif(parametro == 'AX'):
				z += 2
				parametro = parametros[z]
				
				if(parametro == 'p'):
					flag = funcao.ax(parametro)
					z += 2
					analise(z,parametros,flag,count)
						
				elif(parametro == 'q'):
					flag = funcao.ax(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!p'):
					flag = funcao.ax(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!q'):
					flag = funcao.ax(parametro)
					z += 2
					analise(z,parametros,flag,count)
				
				else:
					analise(z,parametros,flag,count)

			elif(parametro == 'AU'):
				z += 2
				parametro = parametros[z]
				
				if(parametro == 'p'):		
					flag = funcao.au(parametro)
					z += 2
					analise(z,parametros,flag,count)
						
				elif(parametro == 'q'):
					flag = funcao.au(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!p'):
					flag = funcao.au(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!q'):
					flag = funcao.au(parametro)
					z += 2
					analise(z,parametros,flag,count)
				
				else:
					analise(z,parametros,flag,count)
				
			elif(parametro == 'EF'):
				z += 2
				parametro = parametros[z]
				
				if(parametro == 'p'):				  
					flag = funcao.ef(parametro)
					z += 2
					analise(z,parametros,flag,count)
						
				elif(parametro == 'q'):
					flag = funcao.ef(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!p'):
					flag = funcao.ef(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!q'):
					flag = funcao.ef(parametro)
					z += 2
					analise(z,parametros,flag,count)
				
				else:
					analise(z,parametros,flag,count)
				
			elif(parametro == 'EG'):
				z += 2   
				parametro = parametros[z]
				
				if(parametro == 'p'):				
					flag = funcao.eg(parametro)
					z += 2
					analise(z,parametros,flag,count)
						
				elif(parametro == 'q'):						
					flag = funcao.eg(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!p'):
					flag = funcao.eg(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!q'):   
					flag = funcao.eg(parametro)
					z += 2
					analise(z,parametros,flag,count)
				
				else:
					analise(z,parametros,flag,count)
				
			elif(parametro == 'EX'):				
				z += 2
				parametro = parametros[z]
				
				if(parametro == 'p'):				
					flag = funcao.ex(parametro)
					z += 2
					analise(z,parametros,flag,count)  

				elif(parametro == 'q'):						
					flag = funcao.ex(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!p'):
					flag = funcao.ex(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!q'): 
					flag = funcao.ex(parametro)
					z += 2
					analise(z,parametros,flag,count)
				
				else:
					analise(z,parametros,flag,count)

			elif(parametro == 'EU'):
				z += 2
				parametro = parametros[z]
				
				if(parametro == 'p'):					
					flag = funcao.eu(parametro)
					z += 2
					analise(z,parametros,flag,count)						

				elif(parametro == 'q'):						
					flag = funcao.eu(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!p'):
					flag = funcao.eu(parametro)
					z += 2
					analise(z,parametros,flag,count)

				elif(parametro == '!q'):
					flag = funcao.eu(parametro)
					z += 2
					analise(z,parametros,flag,count)
				
				else:
					analise(z,parametros,flag,count)

			else:
				print ("Entrada nao reconhecida!") 
		else:
			print(flag)
		  

# Tratamento de cada operador CTL

class  funcao:

	def af(parametro):		
		estadosParamValido = []
		novaIteracao = 1

		for estado in maquina.listaEstados:
			for prop in estado.props:
				if(prop == parametro):
					estadosParamValido.append(estado.num)
					estado.props.append('AF'+parametro)
		
		while (novaIteracao == 1):
			for estado in maquina.listaEstados:
				estadoValido = 1
				for proximo in estado.proxEstados:				
					if (int(proximo) in estadosParamValido) and (estadoValido == 1):
						estadoValido = 1														
					else:
						estadoValido = 0								
				if (estadoValido == 1):	
					estadosParamValido.append(estado.num)
					estado.props.append('AF'+parametro)		
					#novaIteracao = 1
				else:
					novaIteracao = 0			
   
		return True

	def ag(parametro):          
		estadosParamValido = []
		novaIteracao = 1

		for estado in maquina.listaEstados:
			for prop in estado.props:
				if(prop == parametro):
					estadosParamValido.append(estado.num)
					estado.props.append('AG'+parametro)
		
		while (novaIteracao == 1):
			for estado in maquina.listaEstados:
				for proximo in estado.proxEstados:				
					if not (int(proximo) in estadosParamValido) and (estado.num in estadosParamValido):					
						estadosParamValido.remove(estado.num)			
						estado.props.remove('AG'+parametro)								
						#novaIteracao = 1
						#continue
					else:
						novaIteracao = 0
   
		return True

	def ax(parametro):  
		estadosParamValido = []		

		for estado in maquina.listaEstados:
			for prop in estado.props:
				if(prop == parametro):
					estadosParamValido.append(estado.num)			
		
		for estado in maquina.listaEstados:		
			estadoValido = 1				
			for proximo in estado.proxEstados:							
				if (int(proximo) in estadosParamValido) and (estadoValido == 1):
					estadoValido = 1														
				else:
					estadoValido = 0			
			if (estadoValido == 1):	
				estado.props.append('AX'+parametro)																	 

		return True
		
	def au(parametro):
		print('Propriedade não implementada')		           
		return True
	
	def ef(parametro): 
		estadosParamValido = []
		novaIteracao = 1

		for estado in maquina.listaEstados:
			for prop in estado.props:
				if(prop == parametro):
					estadosParamValido.append(estado.num)
					estado.props.append('EF'+parametro)
		
		while (novaIteracao == 1):
			for estado in maquina.listaEstados:
				for proximo in estado.proxEstados:				
					if(int(proximo) in estadosParamValido):
						estadosParamValido.append(estado.num)
						estado.props.append('AF'+parametro)		
						#novaIteracao = 1				
						#continue
					else:
						novaIteracao = 0
   
		return True

	def eg(parametro):      
		estadosParamValido = []
		novaIteracao = 1

		for estado in maquina.listaEstados:
			for prop in estado.props:
				if(prop == parametro):
					estadosParamValido.append(estado.num)
					estado.props.append('EG'+parametro)
		
		while (novaIteracao == 1):
			for estado in maquina.listaEstados:
				estadoValido = 0 # só tiro o estado se nenhum caminho chegar
				for proximo in estado.proxEstados:				
					if not (int(proximo) in estadosParamValido) and (estado.num in estadosParamValido) and (estadoValido == 0):					
						estadoValido = 0														
					else:
						estadoValido = 1
				if (estadoValido == 0):
					estadosParamValido.remove(estado.num)			
					estado.props.remove('EG'+parametro)			
				else:
					novaIteracao = 0
   
		return True
	
	def ex(parametro): #entra quando encontra um rótulo. EXpar vai se tornar o novo parametro para eu analisar! 
		estadosParamValido = []

		for estado in maquina.listaEstados:
			for prop in estado.props:
				if(prop == parametro):
					estadosParamValido.append(estado.num)
		
		for estado in maquina.listaEstados:
			for proximo in estado.proxEstados:				
				if(int(proximo) in estadosParamValido):					
					estado.props.append('EX'+parametro)					
					#continue
   
		return True

	def eu(parametro):
		print('Propriedade não implementada')         
		return True

class maqEstados(object):

	def __init__(self):
		self.listaEstados = []
		self.listaProps = []
		self.listaProxEstados = []

class Estado(object):

	def __init__(self, num, props, proxEstados):
		self.num = num
		self.props = props
		self.proxEstados = proxEstados	

# Leitura do arquivo em um vetor de caracteres

f = open("Rtest.txt", 'r')

arqArray = []
for line in f:
	arqArray.append(line)    
arqArray = [i.split('\n',1)[0] for i in arqArray]
f.close()

# Leitura das propriedades da maquina de estados

totLinhas = int(arqArray[0][0])
	   
for y in range(len(arqArray)):     
	print(arqArray[y])
	
print ('\n')

x = totLinhas + 1 # Expressão a ser avaliada se encontra na linha totLinhas + 1
parametros = arqArray[x]
parametros = parametros.split(' ') # Parametros sao separados por ' '

listaRotulos = []
matrizRotulos = []
listaProxEstad = []
matrizEstados = []
estados = []

for i in range(0, totLinhas):
	totProps = arqArray[i+1][2]
	indexBase = (2*(int(totProps) + 1))
	totProxEstad = arqArray[i+1][indexBase + 2]
	
	# As propriedades da maquina de estados sao preenchidas conforme a posicao
	# das informacoes no arquivo de entrada

	if (totProps == 0):
		listaRotulos = 'None';
	else:
		listaRotulos = (arqArray[i+1][4:(indexBase + 1)]).split(' ')	

	if (totProxEstad == 0):
		listaProxEstad = 'None';
	else:
		listaProxEstad = (arqArray[i+1][(indexBase + 4):(indexBase + (2*int(totProxEstad) + 3))]).split(' ')

	matrizRotulos.append(listaRotulos)		
	matrizEstados.append(listaProxEstad)
	estado = Estado(i+1, listaRotulos, listaProxEstad)
	estados.append(estado)

	print ('Estado:', estado.num)
	print ('Propriedades:', listaRotulos)	
	print ('Proximos Estados:', listaProxEstad, '\n')

print ('Matriz Rotulos:', matrizRotulos)
print ('Matriz Estados:', matrizEstados, '\n')

maquina = maqEstados();
maquina.numEstados = totLinhas
maquina.listaProps = matrizRotulos
maquina.listaProxEstados = matrizEstados
maquina.listaEstados = estados

flag = None
count = 0
analise(0,parametros,flag,count)