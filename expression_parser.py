# coding: utf-8

class treeNode(object):

	def __init__(self):
		self.tipo = None # Operador (Op) ou Propriedade (Pr)
		self.conteudo = None
		self.rotulo = 0
		self.left = None
		self.right = None


class parserCTL():

	def __init__(self)
		self.leftExp = None
		self.rightExp = None
		self.cont = 0 # Controle de abertura e fechamento de parenteses

	def parse(self, exp, pos):
		
		pos = identificaExpressao(exp)


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
				




