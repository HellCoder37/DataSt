from collections import defaultdict
graph =defaultdict (list)
def addedge(graph,u,v):
    graph[u].append(v)
def generate_edge(graph):
    edges=[]
    for node in graph:
        for neighbor in graph:
            edges.append((node,neighbor))
    return edges
addedge(graph,'a','c')
addedge(graph,'b','c')
addedge(graph,'b','e')
addedge(graph,'c','d')
addedge(graph,'c','e')
addedge(graph,'c','a')
addedge(graph,'c','b')
addedge(graph,'e','b')
addedge(graph,'d','c')
addedge(graph,'e','c')
print(generate_edge(graph))