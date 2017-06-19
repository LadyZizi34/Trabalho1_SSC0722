# coding: utf-8

class treeNode(object):

	def __init__(self):
		self.tipo = None # Operador (Op) ou Propriedade (Pr)
		self.conteudo = None
		self.oper = None
		self.rotulo = 0 #precisa??
		self.left = None
		self.right = None


class parserCTL():

	def __init__(self):
		#self.leftExp = None
		#self.rightExp = None
		self.cont = 0 # Controle de abertura e fechamento de parenteses
		self.listaNos = []
		self.expressao = None

	def parse(self, exp):
		
		pos = self.identificaExpressao(exp)
		no = treeNode()

		# Cria nó do tipo Propriedade e 
		# interrompe a recursão
		if (pos == -1):						
			no.tipo = 'Pr'
			no.conteudo = exp[1:(int(len(exp))-1)]
			no.oper = None
			no.left = None
			no.right = None
			self.listaNos.append(no)
			self.expressao = exp
			return no

		# Le próximo operador
		operador = ""		
		i = pos
		while (exp[i] != '('):
			operador += exp[i]
			i += 1

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

		# Há controle de posição do início da expressão e de 
		# onde ocorre a vírgula que separa as duas expressões
		# resultantes. Nas funções AU, -> e <->, precisa-se
		# armazenar as expressões à esquerda e à direita da
		# vírgula/operador para realizar a substituição pela
		# expressão equivalente.

		elif (operador == "AU"):
			pos += 2
			temp = self.lePropriedade(exp, pos)
			virgula = self.identificaExpressao(temp)
			expEsquerda = self.lePropriedade(temp, 1)
			virgula += 1
			expDireita = self.lePropriedade(temp, virgula)
			exp = "((AF" + expDireita + ")&(!(EU((!" + expDireita + "),((!" + expEsquerda + ")&(!" + expDireita + "))))))"
			operador = "&"
			pos = self.identificaExpressao(exp)

		elif (operador == "->"):
			pos += 2
			expEsquerda = self.lePropriedade(exp, 1)
			expDireita = self.lePropriedade(exp, pos)
			exp = "((!" + expEsquerda + ")|" + expDireita + ")"
			operador = "|"
			pos = self.identificaExpressao(exp)				

		elif (operador == "<->"):
			pos += 3
			expEsquerda = self.lePropriedade(exp, 1)
			expDireita = self.lePropriedade(exp, pos)
			exp = "(((!" + expEsquerda + ")|" + expDireita + ")&((!" + expDireita + ")|" + expEsquerda + "))"				
			operador = "&"
			pos = self.identificaExpressao(exp)

		# Após feitas as devidas substituições por
		# expressões equivalentes, analisa-se os opera-
		# dores finais para encerrar o mapeamento da
		# expressão lida em árvore sintática. Quando 
		# um nó da árvore possui apenas um filho, 
		# adota-se que este é seu filho esquerdo.

		no = treeNode()
		no.tipo = 'Op'
		no.conteudo = exp
		no.oper = operador
		
		if(operador == "EX"):
			pos += 2
			expEsquerda = self.lePropriedade(exp, pos)								
			no.left = self.parse(expEsquerda)			

		elif(operador == "AF"):
			pos += 2
			expEsquerda = self.lePropriedade(exp, pos)								
			no.left = self.parse(expEsquerda)			

		elif(operador == "EU"):
			pos += 2
			temp = self.lePropriedade(exp, pos)
			virgula = self.identificaExpressao(temp)
			expEsquerda = self.lePropriedade(temp, 1)
			virgula += 1
			expDireita = self.lePropriedade(temp, virgula)								
			no.left = self.parse(expEsquerda)			
			no.right = self.parse(expDireita)	
									
		elif(operador == "&"):
			expEsquerda = self.lePropriedade(exp, 1)
			pos += 1
			expDireita = self.lePropriedade(exp, pos)					
			no.left = self.parse(expEsquerda)
			no.right = self.parse(expDireita)

		elif(operador == "|"):
			expEsquerda = self.lePropriedade(exp, 1)
			pos += 1
			expDireita = self.lePropriedade(exp, pos)					
			no.left = self.parse(expEsquerda)
			no.right = self.parse(expDireita)			

		elif(operador == "!"):
			pos += 1			
			expEsquerda = self.lePropriedade(exp, pos)					
			no.left = self.parse(expEsquerda)			

		else:
			print("Operador Invalido.")
			exit(1)

		self.listaNos.append(no)
		self.expressao = exp
		return no
	

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
			elif (cont == 1):			
				j = i
				while(exp[j] != '('):					
					if (exp[j] == ')'):
						isProp = True
						break
					j += 1
				if not isProp:
					return i
		return -1

	# Encontra propriedade a partir de uma posição
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