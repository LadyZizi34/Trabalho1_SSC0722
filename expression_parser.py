# coding: utf-8

class noArvore(object):

	def __init__(self):
		self.tipo = None # Operador (Op) ou Propriedade (Pr)
		self.conteudo = None
		self.rotulo = 0 #precisa??
		self.left = None
		self.right = None


class parserCTL():

	def __init__(self):
		self.leftExp = None
		self.rightExp = None
		self.cont = 0 # Controle de abertura e fechamento de parenteses
		self.listaNos = []

	def parse(self, exp, pos):
		
		pos = self.identificaExpressao(exp)

		# Cria nó do tipo Propriedade e 
		# interrompe a recursão
		if (pos == -1):			
			noFolha = noArvore()
			noFolha.tipo = 'Pr'
			noFolha.conteudo = exp[1:(int(len(exp))-1)]
			return noFolha

		# Le próximo operador
		operador = ""		
		while (exp[pos] != '('):
			operador += exp[pos]
			pos += 1
		

		print (operador) ###################

		# Le os operadores e analisa a expressao sobre a
		# qual atuam. Operadores AX, EF, AG, EG, AU, ->
		# e <-> são substituidos por seus equivalentes, de
		# forma que estes operadores não estarão presentes
		# na expressão final. O índice de posição passa a
		# apontar para o restante da expressão.

		if (operador == "AX"):
			pos +=2 
			self.leftExp = 	lePropriedade(exp, pos)
			

		elif (operador == "EF"):

		elif (operador == "AG"):

		elif (operador == "EG"):

		elif (operador == "AU"):

		elif (operador == "->"):

		elif (operador == "<->"):


	# Retorna posição do próximo operador da expressão. Caso
	# essa expresão seja uma propriedade (nó folha), retorna -1
	def identificaExpressao(self, exp):
		cont = 0
		isProp = False
		
		for i in range(0, int(len(exp))):
			# Leitura de operadores básicos
			if (exp[i] == '('):
				cont += 1			
			elif (exp[i] == ')'):
				cont -= 1	
			# Se encontrou algum parâmetro, verifica se
			# é um operador (próximo parenteses abre) ou
			# propriedade (próximo parenteses fecha)
			else:
				j = i
				while(exp[j] != '('):					
					if (exp[j] == ')'):
						isProp = True
						break
					j += 1
				if ((cont == 1) and not isProp):
					return i
				else:
					return -1
				


#class equivlenciaOperadores():



	#def lePropriedade(self, exp, pos):
	#	propriedade = ""
	#	count = 

