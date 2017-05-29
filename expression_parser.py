# coding: utf-8

class treeNode(object):

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
			noFolha = treeNode()
			noFolha.tipo = 'Pr'
			noFolha.conteudo = exp[1:(int(len(exp))-1)]
			return noFolha

		# Le próximo operador
		operador = ""		
		i = pos
		while (exp[i] != '('):
			operador += exp[i]
			i += 1

		print (operador, pos) ###################

		# Le os operadores e analisa a expressao sobre a
		# qual atuam. Operadores AX, EF, AG, EG, AU, ->
		# e <-> são substituidos por seus equivalentes, de
		# forma que estes operadores não estarão presentes
		# na expressão final. O índice de posição passa a
		# apontar para o restante da expressão.

		if (operador == "AX"):			
			pos +=2 			
			#self.leftExp = lePropriedade(exp, pos)
			exp = "(!(EX(!" + self.lePropriedade(exp, pos) + ")))"
			operador = "!" # Novo último operador
			pos = 1 # Índice aponta para o restante da expressão			
	
		elif (operador == "EF"):
			pos += 2
			exp = "(EU((TRUE)," + self.lePropriedade(exp, pos) + "))"
			operador = "EU"
			pos = 1

		elif (operador == "AG"):
			pos += 2
			exp = "(!(EU((TRUE),(!" + self.lePropriedade(exp, pos) + "))))"
			operador = "!"
			pos = 1			

		elif (operador == "EG"):
			pos += 2
			exp = "(!(AF(!" + self.lePropriedade(exp, pos) + ")))"
			operador = "!"
			pos = 1	

		elif (operador == "AU"):
			pos

		elif (operador == "->"):

		elif (operador == "<->"):


	def converte_au_afeu(self, esquerda, direita):
		return "((AF" + direita + ")&(!(EU((!" + direita + "),((!" + esquerda + ")&(!" + direita + "))))))"

	def converte_impsimples(self, esquerda, direita):
		return "((!" + esquerda + ")|" + direita + ")"

	def converte_impduplo(self, esquerda, direita):
		return "(((!" + esquerda + ")|" + direita + ")&((!" + direita + ")|" + esquerda + "))"				
			
	
	
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
					print ('Find Func', i)
					return i
				else:
					return -1
				

	def lePropriedade(self, exp, pos):
		propriedade = "("
		contador = 1
		pos += 1
		while(contador != 0):			
			propriedade += exp[pos]
			if(exp[pos] == '('):
				contador += 1
			elif(exp[pos] == ')'):
				contador -= 1
			pos += 1
		return propriedade

	

