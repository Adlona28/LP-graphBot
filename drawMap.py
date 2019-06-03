from staticmap import StaticMap, CircleMarker, Line
import networkx as nx
from haversine import haversine

def plotpop(dist, latitude, longitude):
    m = StaticMap(400, 400)
    m.add_line(Line(((13.4, 52.5), (2.3, 48.9)), 'blue', 3))
    image = m.render()
    image.save('map.png')

plotpop(3,3,3)