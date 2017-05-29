# coding: utf-8

class treeNode(object):

	def __init__(self):
		self.tipo = None # Operador ou Propriedade
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


	def identificaExpressao(self, exp):
		int cont = 0
		for i in range(0, int(len(exp))):
			# Leitura de operadores básicos
			if (exp[i] == '('):
				cont += 1			
			elif (exp[i] == ')'):
				cont -= 1	
			# Caso contrário, verifica se é folha			
			else:
				while 

