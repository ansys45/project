import matplotlib.pyplot as plt
import networkx as nx
import re
import random
import community
from karger import change_graph, remove_loops, choose_random_edge, contract_edge


# dfs algorythm to find all connected components in order to find the largest one to apply kargers algorythm to it
def dfs(graph, vertex, path=set()):
    path.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs(graph, neighbor, path)

    return path

# parsing file with memebers of group and creating list of them
people = []
with open("t.txt", "r") as f:
    i = 0
    for i in f.readlines():
        i = i.replace("[", "")
        i = i.replace("'", "")
        i = i.split("]")
        k = 0
        for person in i:
            person = person.replace(" ", "")
            person = person.split(",")
            # was 4
            if len(person) != 3:
                continue
            people.append(person[1:])

# creating dictionary which represents the graph
g = {}
for person1 in people:
    g[person1[0]] = []
    for person2 in people:
        if person1[1] == person2[1] and person1 != person2:
            g[person1[0]].append(person2[0])

# applying dfs algorythm to find all connected components and idetify the biggest one
pathes = []
cc = []
for i in g:
    pathes.append(dfs(g, i, path = set()))

for i in pathes:
    if len(i) > len(cc):
        cc = i

# creating subgraph
connected_component = {}
for i in cc:
    connected_component[i] = g[i]

# change form of the graph to apply karger's algorythm
new_g = change_graph(connected_component)

# applying karger's algorythm
while len(new_g) > 2:
    contract_edge(choose_random_edge(new_g), new_g)


# writting result in file
file = open("karger.txt", 'a')
for i in new_g:
    print(i, file = file)
    mincut = len(new_g[i])
print(mincut)
file.close()

# drawing the graph (nodes are people; nodes are connected if poeple are from the same city)
graph = nx.Graph()
for person in people:
    graph.add_node(person[0])
for person1 in people:
    for person2 in people:
        if (person1[1] == person2[1]):
            graph.add_edge(person1[0], person2[0])
nx.draw(graph, node_size=50, with_labels=True, font_size=10)
plt.show()

# finding and drawing communitites after lui_vain algorythm
file_lui = open("lui_vain.txt", "a")
partition = community.best_partition(graph)
best_graph = nx.Graph()
best_graph.add_edges_from([edge for edge in partition.items() if edge[1] == 1])
print(best_graph.nodes(), file=file_lui)
nx.draw(best_graph, node_size=50, with_labels=True, font_size=10)
plt.show()
file_lui.close()
