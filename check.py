import csv
import networkx as nx
from haversine import haversine
import genGraph

def naifFormToCheck(population, distance):
	L = []
	with open('./worldcities.csv') as file:
		readCSV = csv.reader(file, delimiter=',')
		id = 0
		for row in readCSV:
			if row[4] != "" and float(row[4]) >= population:
				L.append([row[0], row[1], float(row[5]), float(row[6]), id])
				id = id+1		
	file.close()
	G = nx.Graph()

	for n in L:
		G.add_node(n[4], country=n[0], city=n[1],
		latitude=n[2], longitude=n[3])

	for n in L:
		for k in L:
			if haversine((n[2], n[3]), (k[2], k[3])) <= distance and n[4] != k[4]:
				G.add_edge(n[4], k[4])
	print(G.number_of_nodes())
	print(G.number_of_edges())
	return G

naifG = naifFormToCheck(100000, 300)
coolG = genGraph.genGraph(100000, 300)
print()
print()
print()
print()
print("---------")
print(naifG.number_of_nodes())
print(naifG.number_of_edges())
print("--")
print(coolG.number_of_nodes())
print(coolG.number_of_edges())
print("---------")
print()
print()
print()
print()
naifL = list(naifG.nodes)
coolL = list(coolG.nodes)
count = 0