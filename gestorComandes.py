import genGraph
import drawMap
import networkx as nx

def graph(args):
	G = genGraph.genGraph(int(args[1]), int(args[0]))
	return G

def components(G):
	return nx.number_connected_components(G)

def plotpot(dist, lat, lon, G):
	return drawMap.drawPop(dist, lat, lon, G)