# coding: utf-8

class maqEstados(object):

	def __init__(self):
		self.listaEstados = []
		self.listaProps = []
		self.listaProxEstados = []
		self.numEstados = 0

	def leMaquina(self, arqArray):
		# Leitura das propriedades da maquina de estados

		totLinhas = int(arqArray[0][0])		

		if (totLinhas <= 0) or (totLinhas != (len(arqArray) - 2)): # Confere integridade da máquina
			return False

		listaPropriedades = []
		matrizProps = []
		listaProxEstad = []
		matrizEstados = []
		estados = []

		for i in range(0, totLinhas):
			totProps = arqArray[i+1][2]
			indexBase = (2*(int(totProps) + 1))
			totProxEstad = arqArray[i+1][indexBase + 2]
			
			# As propriedades da maquina de estados sao preenchidas conforme a posicao
			# das informacoes no arquivo de entrada

			if (totProps == 0):
				listaPropriedades = 'None';
			else:
				listaPropriedades = (arqArray[i+1][4:(indexBase + 1)]).split(' ')	

			if (totProxEstad == 0):
				listaProxEstad = 'None';
			else:
				listaProxEstad = (arqArray[i+1][(indexBase + 4):(indexBase + (2*int(totProxEstad) + 3))]).split(' ')
				for j in listaProxEstad:
					if (int(j) > totLinhas): 
						return False

			matrizProps.append(listaPropriedades)		
			matrizEstados.append(listaProxEstad)
			estado = Estado(i+1, listaPropriedades, listaProxEstad)
			estados.append(estado)

			print ('Estado', estado.num)
			print ('Propriedades:', listaPropriedades)	
			print ('Proximos Estados:', listaProxEstad, '\n')

		# Definição da Máquina de Estados

		self.numEstados = totLinhas
		self.listaEstados = estados
		self.listaProps = matrizProps
		self.listaProxEstados = matrizEstados

		print ('Matriz Propriedades:', matrizProps)
		print ('Matriz Estados:', matrizEstados, '\n')

		

		return True


class Estado(object):

	def __init__(self, num, props, proxEstados):
		self.num = num
		self.props = props
		self.proxEstados = proxEstados

