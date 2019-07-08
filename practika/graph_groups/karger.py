import random

def change_graph(g):
    new_g = {}
    for i in g:
        s = (i,)
        new_g[s] = g[i]
    return new_g


def remove_loops(value, key):
    l = len(value)
    for i in value:
        if i in key:
            value.remove(i)
    if len(value) < l:
        return remove_loops(value, key)

def choose_random_edge(g):
    i = random.randrange(len(g) - 1)
    k = 0
    for v in g:
        v1 = v
        k += 1
        if k == i:
            break
    if len(g[v1]) == 1:
        v2 = (g[v1][0],)
        return (v1, v2)
    i = random.randrange(len(g[v1]))
    k = 0
    for v in g[v1]:
        v2 = (v,)
        k += 1
        if k == i:
            break
    return (v1, v2)

def contract_edge(edge, g):
    v1 = edge[0]
    v2 = edge[1]
    for node in g:
        for i in v1:
            if i in node:
                v1 = node
                break
        for i in v2:
            if i in node:
                v2 = node
                break
    l = list(v1)
    for i in v2:
        l.append(i)
    merge_v = tuple(l)
    l = g[v1]
    for i in g[v2]:
        g[v1].append(i)
    g[merge_v] = g[v1]

    remove_loops(g[merge_v], merge_v)

    del g[v1]
    del g[v2]


def merge(graph, u1, u2):
    for node in graph[u2]:
        if node != u1:
            graph[u1].append(node)
        graph[node].remove(u2)
        if node != u1:
            graph[node].append(u1)
    del graph[u2]


def Kar(graph):
    temp = {k : str(i) for (i, k) in enumerate(graph.keys(), 0)}
    while len(graph) > 2:
        u1 = random.choice(list(graph.keys()))
        u2 = random.choice(graph[u1]) 
        id_ = temp[u2]
        for key in temp.keys():
            if(temp[key] == id_):
                temp[key] = temp[u1]
        merge(graph, u1, u2)

    mincut = len(graph[list(graph.keys())[0]])
    return mincut