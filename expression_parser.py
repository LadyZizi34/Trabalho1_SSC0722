# coding: utf-8

class treeNode(object):

	def __init__(self):
		self.tipo = None # Operador ou Propriedade
		self.conteudo = None
		self.rotulo = 0
		self.left = None
		self.right = None


class parserCTL():

	def parse(self, expList):
		print ('ola')