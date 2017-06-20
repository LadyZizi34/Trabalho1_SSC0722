# coding: utf-8
import sys
from state_machine_reader import maqEstados
from expression_parser import parserCTL
from verifier import verificadorAvSintatica

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
	
print(" ")
maquina = maqEstados()

if not (maquina.leMaquina(arquivo)):
	sys.exit("Máquina de Estados inválida.\n")

print("Expressao:", expressao)
arvoreSintatica = parserCTL()
arvoreSintatica.parse(expressao)
expressaoEquivalente = arvoreSintatica.expressao
listaDeNos = []

print("\nArvore:")
for i in reversed(range(0, int(len(arvoreSintatica.listaNos)))):
	print (arvoreSintatica.listaNos[i].conteudo)
	#listaDeNos.append(arvoreSintatica.listaNos[i])

print("\nEstados validos:")
verificador = verificadorAvSintatica(listaDeNos, maquina)
#print(verificador.estados[2].num)
#print(arvoreSintatica.listaNos[0].conteudo)
verificador.preenchePilha(arvoreSintatica.listaNos)

for estado in maquina.listaEstados:
	if expressaoEquivalente in estado.expValidas:
		print(estado.num, end=" ")

print("")


