''' Note that when you are running this program, it will show you all euler circuit then after probability.
  what you have to do is just keep closing the graph untill finish, then it will return the probability in python console '''
# these are imported libraries required in these program
import matplotlib.pyplot as plt  # used for to plot some lines in a plotting area,
import networkx as nx  # used to create, manipulate graph networks.
from itertools import combinations  # this is for making combination of vertices in this program
from random import random  # this is for generating things randomly


# this is where our function started for combining vertices randomly
def ER(nbr, probability,    count_connected, count_euler_circuit):
    Vertice = set([v for v in range(nbr)])
    Edges = set()
    for combination in combinations(Vertice, 2):  # this for making a combination of two vertices
        a = random()  # this is for generating combination randomly
        if a < probability:
            Edges.add(combination)  # this is a list for holding the combinations generated such as nodes

    g = nx.Graph()  # this is for generating ploting edges/line between vertices
    g.add_nodes_from(Vertice)
    g.add_edges_from(Edges)

    connect = nx.is_connected(g)   # this is for counting the out put of graph which is connected
    circuit = nx.is_eulerian(g)    # this for counting the out put of graph which is euler circuit

    # if graph is connected, add one to the count_connect
    if connect ==True:
       count_connected += 1

       # if is euler circuit add one on count_euler_circuit
       if circuit == True:
         count_euler_circuit += 1

         pos = nx.spring_layout(g)
         nx.draw_networkx(g, pos)
         plt.title(" euler circuit graph")
         plt.show()

    return count_connected, count_euler_circuit    # calling function


nbr = 10
probability = 0.4
count_connected = 0
count_euler_circuit = 0

# this is the estimated number we need to determine probability of getting euler circuit based on.
for x in range(3000):
    count_connected, count_euler_circuit =ER(nbr, probability, count_connected,count_euler_circuit)

''' we used try and exception to capture up error when for count_connected is 0 
because we can not divid by zero '''
''' then probability is determined by dividing number of euler circuit occured over 
    number of connected graph happened in the sample of 3000'''
try:
    probability_ofgetting_euler_circuit = count_euler_circuit/count_connected
    print("the probability of getting euler circuit is:\n", probability_ofgetting_euler_circuit)
except ZeroDivisionError as exception:
    print(exception)
