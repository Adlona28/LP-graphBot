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
    kmPerGrau = kmPerGrau + 5
    return normalizedLong(longitud + int(distance/kmPerGrau))


def getKey(item):
    return item[3]


def graph(N, M):
    G = nx.Graph()
    for node in N:
        G.add_node(node[1], country=node[0], lat=node[2], long=node[3])
    G.add_edges_from(M)
    return G


def readFile(population):
    L = []
    with open('./worldCitiesWithPopulation.csv') as file:
        readCSV = csv.reader(file, delimiter=',')
        for row in readCSV:
            if float(row[2]) >= population:
                L.append([row[0], row[1], float(row[3]), float(row[4])])
    file.close()
    L.sort(key=getKey)
    return L


def genEdges(L, distance):
    A = []
    i = 0
    while i < len(L):
        longLimit = coordLimit(distance, L[i][2], L[i][3])
        longActual = L[i][3]
        j = i
        while longActual <= longLimit and j < len(L):
            if haversine((L[i][2], L[i][3]), (L[j][2], L[j][3])) <= distance:
                A.append([L[i][1], L[j][1]])
            longActual = L[j][3]
            j = j + 1
        i = i+1
    print(len(L))
    print(len(A))
    return A


def genGraph(population, distance):
    L = readFile(population)
    A = genEdges(L, distance)
    return graph(L, A)


genGraph(100000, 300)
