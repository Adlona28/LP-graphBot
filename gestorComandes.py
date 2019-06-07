import genGraph
import drawMap
import networkx as nx
from fuzzywuzzy import fuzz


def graph(args):
    G = genGraph.genGraph(int(args[1]), int(args[0]))
    return G


def components(G):
    return nx.number_connected_components(G)


def plotpot(dist, lat, lon, G):
    return drawMap.drawPop(float(dist), float(lat), float(lon), G)


def plotgraph(dist, lat, lon, G):
    return drawMap.drawGraph(float(dist), float(lat), float(lon), G)


def route(args, G):
    L = []
    for i in range(len(args)):
        word = ''
        for char in args[i]:
            if char != '"' and char != ',':
                word += char
        L.append(word)
    srcCity = L[0]
    srcCountry = L[1]
    destCity = L[2]
    destCountry = L[3]
    nodeSrc = 0
    ratioNodeSrc = 0
    nodeDest = 0
    ratioNodeDest = 0
    for node in list(G.nodes):
        if srcCountry == G.nodes[node]['country']:
            ratio = fuzz.ratio(srcCity, G.nodes[node]['city'])
            if ratio > ratioNodeSrc:
                nodeSrc = node
                ratioNodeSrc = ratio
        if destCountry == G.nodes[node]['country']:
            ratio = fuzz.ratio(destCity, G.nodes[node]['city'])
            if ratio > ratioNodeDest:
                nodeDest = node
                ratioNodeDest = ratio
    path = nx.shortest_path(G, source=nodeSrc, target=nodeDest)
    return drawMap.drawRoute(G, path)
