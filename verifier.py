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

		pilhaTemp.append(lista[len(lista)-1]) # Insere nó raiz

	# Primeiramente deve-se construir uma pilha onde
	# o nó raiz esteja na base e os nós folha, no topo.
	# Assim, será possível realizar a marcação 'de baixo
	# para cima'
		while pilhaTemp:
			atual = pilhaTemp.pop()
			pilhaFinal.append(atual)
			if atual.left:				
				pilhaTemp.append(atual.left)
			if atual.right:				
				pilhaTemp.append(atual.right)

		while pilhaFinal:
			atual = pilhaFinal[len(pilhaFinal)-1]
			if (atual.tipo == 'Op'):
				if(atual.oper == "EX"):
					self.ex(atual.left.conteudo, atual.conteudo)
				elif(atual.oper == "AF"):
					self.af(atual.left.conteudo, atual.conteudo)
				elif(atual.oper == "EU"):
					self.eu(atual.left.conteudo, atual.right.conteudo, atual.conteudo)					
				elif(atual.oper == "!"):
					self.op_not(atual.left.conteudo, atual.conteudo)
				elif(atual.oper == "&"):
					self.op_and(atual.left.conteudo, atual.right.conteudo, atual.conteudo)
				elif(atual.oper == "|"):
					self.op_or(atual.left.conteudo, atual.right.conteudo, atual.conteudo)
				else:
					print("Máquina de Estados mal formada.")
			else:				
				self.op_add(atual.conteudo) # Adiciona as propriedades às expressões válidas

			pilhaFinal.pop()


	def ex(self, expLeft, exp): #entra quando encontra um rótulo. EXpar vai se tornar o novo parametro para eu analisar! 
		for estado in self.estados:
			estadoValido = False
			if exp not in estado.expValidas:
				estadoValido = True		
			if expLeft in estado.proxEstados:				
				if estadoValido:					
					estado.expValidas.append(exp)					
					break;

	def af(self, expLeft, exp):				
		novaIteracao = True

		for estado in self.estados:
			if expLeft in estado.expValidas:				
				estado.expValidas.append(exp)
		
		while (novaIteracao):
			novaIteracao = False
			for estado in self.estados:
				estadoValido = True
				if exp not in estado.expValidas:
					estadoValido = True 
					for proximo in estado.proxEstados:				
						if exp not in proximo.expValidas:
							estadoValido = False
							break																						
					if estadoValido and (not len(estado.proxEstados) == 0):	
						estado.expValidas.append(exp)		
						novaIteracao = True					

	def eu(self, expLeft, expRight, exp):
		novaIteracao = True

		for estado in self.estados:
			if expRight in estado.expValidas:				
				estado.expValidas.append(exp)		

		while (novaIteracao):
			novaIteracao = False
			for estado in self.estados:				
				if ((expLeft in estado.expValidas) or expLeft == "TRUE") and (exp not in estado.expValidas):								
					for proximo in estado.proxEstados:				
						if exp in proximo.expValidas:						
							estado.expValidas.append(exp)		
							novaIteracao = True								
							break
				
	def op_not(self, expLeft, exp):
		for estado in self.estados:
			if expLeft not in estado.expValidas:
				estado.expValidas.append(exp)

	def op_and(self, expLeft, expRight, exp):
		for estado in self.estados:
			if (expLeft in estado.expValidas) and (expRight in estado.expValidas):
				estado.expValidas.append(exp)
	
	def op_or(self, expLeft, expRight, exp):
		for estado in self.estados:
			if (expLeft in estado.expValidas) or (expRight in estado.expValidas):
				estado.expValidas.append(exp)			

	def op_add(self, exp):
		for estado in self.estados:					
			if exp in estado.props:								
				estado.expValidas.append(exp)

