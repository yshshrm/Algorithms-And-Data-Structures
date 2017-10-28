#kruskal's algorithm for minimum spanning tree

"""
  **Brief** :Kruskal's algorithm is a minimum-spanning-tree algorithm which finds an edge of the least possible weight that connects any two trees in the forest.It is a greedy algorithm in graph theory as it finds a minimum spanning tree for a connected weighted graph adding increasing cost arcs at each step. The algorithm is implemented using disjoint-set data structure here.


  **Complexity** :O(ElogE) OR O(ElogV) where E and V are the number of edges and vertices respectively

  **Applications** :Most of the cable network companies use the Disjoint Set Union data structure in Kruskal’s algorithm to find the shortest path to lay cables across a city or group of cities.

"""

parent = dict()                     #intializing a new empty dictionary named parent. This will contain the parent vertices of each vertice
rank = dict()                       #intitializing a new empty dictionary named rank. This will hold the rank of each vertice

def make_set(vertice):              #this function will create a set out of a single vertice
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):                  #this function returns the parent of the given vertice in the argument. It is a recursive function.
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:           #creating an entry for each vertice of the graph in the the parent and rank dictionaries using the make_set function
        make_set(vertice)

    minimum_spanning_tree = set()               #initializing the minimum spanning tree as a set data structure. This set will keep expanding until we get the final set at the end of this function.

    edges = list(graph['edges'])                #edges is the list of all the edges of the graph. each edge is represented as a dictionary with the following keys: (weight,vertice1,vertice2)
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
return minimum_spanning_tree
