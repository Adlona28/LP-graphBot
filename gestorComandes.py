import genGraph
import drawMap

def graph(args):
	print('recibo la llamada')
	G = genGraph.genGraph(args[1], args[0])
	print('generated')
	return G

#graph([300, 100000])