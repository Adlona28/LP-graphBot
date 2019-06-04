from staticmap import StaticMap, CircleMarker, Line
import networkx as nx
from haversine import haversine
import genGraph
import time

def nodesAtDistFrom(dist, lat, lon, graph):
    G = graph.copy()
    maxPop = 0
    for n in list(G.nodes):
        if not haversine((G.nodes[n]['latitude'], G.nodes[n]['longitude']), (lat, lon)) <= dist:
            G.remove_node(n)
        elif G.nodes[n]['pop'] > maxPop:
            maxPop = G.nodes[n]['pop']
    return [G, maxPop]


def drawPop(dist, lat, lon, graph):
    m = StaticMap(400, 400)
    returned = nodesAtDistFrom(dist, lat, lon, graph)
    G = returned[0]
    maxPop = returned[1]
    for node in list(G.nodes):
        m.add_marker(CircleMarker((G.nodes[node]['longitude'], G.nodes[node]['latitude']), 'red', max(3, G.nodes[node]['pop'] * 15 / maxPop)))
    image = m.render()
    image.save('plotpop.png')


def drawGraph(dist, lat, lon, graph):
    m = StaticMap(400, 400)
    returned = nodesAtDistFrom(dist, lat, lon, graph)
    G = returned[0]
    for node in list(G.nodes):
        m.add_marker(CircleMarker((G.nodes[node]['longitude'], G.nodes[node]['latitude']), 'red', 3))
        for connection in list(G.adj[node]):
            m.add_line(Line(((G.nodes[node]['longitude'], G.nodes[node]['latitude']), (G.nodes[connection]['longitude'], G.nodes[connection]['latitude'])), 'blue', 0))
    image = m.render()
    image.save('plotgraph.png')


def drawRoute(G, path):
    m = StaticMap(400, 400)
    m.add_marker(CircleMarker((G.nodes[path[0]]['longitude'], G.nodes[path[0]]['latitude']), 'red', 3))
    for i in range(len(path) - 1):
        m.add_marker(CircleMarker((G.nodes[path[i+1]]['longitude'], G.nodes[path[i+1]]['latitude']), 'red', 3))
        m.add_line(Line(((G.nodes[path[i]]['longitude'], G.nodes[path[i]]['latitude']), (G.nodes[path[i+1]]['longitude'], G.nodes[path[i+1]]['latitude'])), 'blue', 1))
    image = m.render()
    image.save('plotroute.png')    


#graph = genGraph.genGraph(100000, 300)
#drawPop(1000, 41.47, 2.25, graph)
#drawGraph(1000, 41.47, 2.25, graph)
#drawRoute(graph, [31,32,33])
