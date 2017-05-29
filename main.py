# coding: utf-8
import sys
from state_machine_reader import maqEstados
from expression_parser import parserCTL

# Leitura do arquivo em um vetor de caracteres

f = open("Rtest.txt", 'r')

arquivo = []
for line in f:
	arquivo.append(line)    
arquivo = [i.split('\n',1)[0] for i in arquivo]
f.close()

index = int(arquivo[0][0]) + 1 # Expressão a ser avaliada se encontra na linha 'numero de estados + 1'
expressao = arquivo[index]
#parametros = arquivo[index].split(' ') #-------------

for y in range(len(arquivo)):     
	print(arquivo[y])
	
#expressao = ''.join(parametros)
print ('\nExpressao:', expressao, '\n')

maquina = maqEstados()

if not (maquina.leMaquina(arquivo)):
	sys.exit("Máquina de Estados inválida.\n")

parser = parserCTL()
#verificacao parenteses: verifEstrutura(self, exp)
parser.parse(expressao, 0)





