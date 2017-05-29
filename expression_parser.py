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
		while (exp[pos] != '('):
			operador += exp[pos]
			pos += 1
		print (operador)



		


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
				

	def leExpressao(self, exp, pos):
		expressao = ""
		while(exp[pos] != '('):
			expressao += exp[i]
			pos++
		return expressao

	def lePropriedade(self, exp, pos):
		propriedade = "("
		contador = 1
		pos++
		while(contador != 0):
			propriedade += exp[pos]
			if(exp[pos] == '('):
				contador++
			else if(exp[pos] == ')'):
				contador--
		return propriedade

	def converte_ax_ex(self, string):
		return "(!(EX(!" + string + ")))"

	def converte_ef_eu(self, string):
		return "(EU((TRUE)," + string + "))"

	def converte_ag_eu(self, string):
		return "(!(EU((TRUE),(!" + string + "))))"

	def converte_eg_af(self, string):
		return "(!(AF(!" + string + ")))"

	def converte_au_afeu(self, esquerda, direita):
		return "((AF" + direita + ")&(!(EU((!" + direita + "),((!" + esquerda + ")&(!" + direita + "))))))"

	def converte_impsimples(self, esquerda, direita):
		return "((!" + esquerda + ")|" + direita + ")"

	def converte_impduplo(self, esquerda, direita):
		return "(((!" + esquerda + ")|" + direita + ")&((!" + direita + ")|" + esquerda + "))"