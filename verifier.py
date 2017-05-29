# coding: utf-8

class verificadorAvSintatica(object):

	def __init__(self, nosArvore, maq):
		self.rotulos = int(len(nosArvore))
		self.nos = nosArvore
		self.estados = maq.listaEstados
		self.pilha = []

	def preenchePilha(self, lista):
	# Primeiramente deve-se construir uma pilha onde
	# o nó raiz esteja na base e os nós folha, no topo.
	# Assim, será possível realizar a marcação 'de baixo
	# para cima'
		while lista:
			atual = lista.pop()
			self.pilha.insert(0,atual)
			if atual.left:
				lista.insert(0,atual.left)
			if atual.right:
				lista.insert(0,atual.right)


		for i in (range(0, int(len(self.pilha)))):
			print (self.pilha[i].conteudo)



	def af(parametro):		
		estadosParamValido = []
		novaIteracao = 1

		for estado in self.estados:
			for prop in estado.props:
				if(prop == parametro):
					estadosParamValido.append(estado.num)
					estado.props.append('AF'+parametro)
		
		while (novaIteracao == 1):
			for estado in self.estados:
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

		for estado in self.estados:
			for prop in estado.props:
				if(prop == parametro):
					estadosParamValido.append(estado.num)
					estado.props.append('AG'+parametro)
		
		while (novaIteracao == 1):
			for estado in self.estados:
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

		for estado in self.estados:
			for prop in estado.props:
				if(prop == parametro):
					estadosParamValido.append(estado.num)			
		
		for estado in self.estados:		
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

		for estado in self.estados:
			for prop in estado.props:
				if(prop == parametro):
					estadosParamValido.append(estado.num)
					estado.props.append('EF'+parametro)
		
		while (novaIteracao == 1):
			for estado in self.estados:
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

		for estado in self.estados:
			for prop in estado.props:
				if(prop == parametro):
					estadosParamValido.append(estado.num)
					estado.props.append('EG'+parametro)
		
		while (novaIteracao == 1):
			for estado in self.estados:
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

		for estado in self.estados:
			for prop in estado.props:
				if(prop == parametro):
					estadosParamValido.append(estado.num)
		
		for estado in self.estados:
			for proximo in estado.proxEstados:				
				if(int(proximo) in estadosParamValido):					
					estado.props.append('EX'+parametro)					
					#continue

		return True		