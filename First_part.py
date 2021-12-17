''' *discrete math summative term 1*.
    this the program designed to return the undirected graph of ten vertices.
     I t will determine if it is connected ad if it has euler circuit or not.
     and again we have an other file for calculating the probability of getting an euler circuit.
      so let jump into the codes and there is comment for understanding the codes about'''

# these are imported libraries required in these program
import matplotlib.pyplot as plt          # used for to plot some lines in a plotting area,
import networkx as nx                 # used to create, manipulate graph networks.
from itertools import combinations    # this is for making combination of vertices in this program
from random import random     # this is for generating things randomly

# this is where our function started for combining vertices randomly
def ER(nbr, probability):
    Vertice = set([v for v in range(nbr)])
    Edges = set()
    for combination in combinations(Vertice, 2):     # this for making a combination of two vertices
        a = random()                  # this is for generating combination randomly
        if a < probability:
            Edges.add(combination)        # this is a list for holding the combinations generated such as nodes

    g = nx.Graph()                        # this is for generating ploting edges/line between vertices
    g.add_nodes_from(Vertice)
    g.add_edges_from(Edges)
    return g


nbr = 10              # number of vertices
probability = 0.4     # probability of having a connection between vertices
G = ER(nbr, probability)
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)

# if the graph is connected it will return true
if nx.is_connected(G) is True:
    print(nx.is_connected(G), ": graph is connected")

# if graph is not connected it will return false
else:
    print(nx.is_connected(G), ": graph is not connected")

# return true if the graph is an euler circuit
if nx.is_eulerian(G) is True:
    print(nx.is_eulerian(G), ": graph is euler circuit")

# return false if the graph is not euler circuit
else:
    print(nx.is_eulerian(G), ": graph is not euler circuit")

# this is a title of graph
plt.title("Undirected Graph Generated")
plt.show()


