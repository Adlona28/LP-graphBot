import csv
import networkx as nx
from haversine import haversine


def normalizedLong(longitud):
    longitud = longitud + 180.0
    longitud = longitud % 360.0
    longitud = longitud - 180.0
    return longitud


def coordLimit(distance, latitude, longitud):
    kmPerGrau = haversine((latitude, 0.0), (latitude, 1.0))
    kmPerGrau = kmPerGrau
    return normalizedLong(longitud + int(distance/kmPerGrau) + 1)


def getKey(item):
    return item[3]


def graph(N, M):
    G = nx.Graph()
    for node in N:
        G.add_node(node[4], country=node[0], city=node[1],
                   latitude=node[2], longitude=node[3])
    G.add_edges_from(M)
    return G


def readFile(population):
    L = []
    with open('./worldCitiesWithPopulation.csv') as file:
        readCSV = csv.reader(file, delimiter=',')
        id = 1
        for row in readCSV:
            if float(row[2]) >= population:
                L.append([row[0], row[1], float(row[3]), float(row[4]), id])
                id = id+1
    file.close()
    L.sort(key=getKey)
    return L


def genEdges(L, distance):
    A = []
    for i in range (len(L)-1):
        longLimit = coordLimit(distance, L[i][2], L[i][3])
        longActual = L[i][3]
        bandera = False
        if longActual > longLimit:
            bandera = True
        j = i
        while bandera or longActual <= longLimit:
            if L[i][4] != L[j][4] and haversine((L[i][2], L[i][3]), (L[j][2], L[j][3])) <= distance:
                A.append([L[i][4], L[j][4]])
            longActual = L[j][3]
            j = j + 1
            if j == len(L):
                if bandera:
                    j = 0
                    bandera = False
                else:
                    longActual = 100000.0
    return A


def genGraph(population, distance):
    L = readFile(population)
    A = genEdges(L, distance)
    print(len(L))
    print(len(A))
    return graph(L, A)


G = genGraph(100000, 300)
print(G.number_of_nodes())
print(G.number_of_edges())
