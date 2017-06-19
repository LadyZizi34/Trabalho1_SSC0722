# coding: utf-8
from expression_parser import treeNode

class verificadorAvSintatica(object):

	def __init__(self, nosArvore, maq):
		self.rotulos = int(len(nosArvore))
		self.nos = nosArvore
		self.estados = maq.listaEstados
		self.pilha = []  ##nao uso?? ---------------

	def preenchePilha(self, lista):

		pilhaTemp = []
		pilhaFinal = []
		atual = treeNode()

		print("Raiz:", lista[len(lista)-1].conteudo)

		pilhaTemp.append(lista[len(lista)-1]) # Insere nó raiz
		print(pilhaTemp)

		print("Lista 0:",lista[0].conteudo)
	# Primeiramente deve-se construir uma pilha onde
	# o nó raiz esteja na base e os nós folha, no topo.
	# Assim, será possível realizar a marcação 'de baixo
	# para cima'
		while pilhaTemp:
			print("Lista:", pilhaTemp)
			print("pop:", pilhaTemp[0])
			atual = pilhaTemp.pop()
			print("atual: ", atual)
			print("Lista:", pilhaTemp)
			print("atual.conteudo:",atual.conteudo)
			pilhaFinal.append(atual)
			if atual.left:
				print("left:", atual.left)
				pilhaTemp.append(atual.left)
			if atual.right:
				print("right:", atual)
				pilhaTemp.append(atual.right)

		print("A lista nova")
		for i in (range(0, int(len(pilhaFinal)))):
			print (pilhaFinal[i].conteudo)

		while pilhaFinal:
			atual = pilhaFinal[len(pilhaFinal)-1]
			print("Content:",atual.conteudo)
			if (atual.tipo == 'Op'):
				if(atual.oper == "EX"):
					self.ex(self.estados, atual.left.conteudo, atual.conteudo)
				elif(atual.oper == "AF"):
					self.af(self.estados, atual.left.conteudo, atual.conteudo)
				elif(atual.oper == "EU"):
					self.eu(self.estados, atual.left.conteudo, atual.right.conteudo, atual.conteudo)					
				elif(atual.oper == "!"):
					self.op_not(self.estados, atual.left.conteudo, atual.conteudo)
				elif(atual.oper == "&"):
					self.op_and(self.estados, atual.left.conteudo, atual.right.conteudo, atual.conteudo)
				elif(atual.oper == "|"):
					self.op_or(self.estados, atual.left.conteudo, atual.right.conteudo, atual.conteudo)
				else:
					print("Máquina de Estados mal formada.")
			else:
				op_add(self.estados, atual.conteudo)

			pilhaFinal.pop()

	def af(self, expLeft, exp):		
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