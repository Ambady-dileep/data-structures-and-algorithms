# 🔑 What is a Graph?
# A Graph is a collection of:

# Nodes (aka vertices) 👉 points

# Edges 👉 connections between those points

# Example: Think of Facebook. Each person = node. Each friendship = edge.

# ✅ Graph Terminology (in Plain English)
# Term	             Meaning	               Example
# Node(Vertex)       A point	             A, B, C, D
# Edge	             A connection	         A → B
# Undirected	     Edge without direction  A-B is same as B-A
# Directed (Digraph) Edge has direction	     A → B is not B → A
# Weighted	         Edge has cost/value	 A -3-> B (weight = 3)
# Unweighted	     No value on edge	     A → B (just a link)
# Degree	         No. of edges on a node	 A has 2 edges → degree = 2

class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edge(self,u,v):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}-->{self.graph[vertex]}")
        
class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edge(self, u, v):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)
    def display(self):
        for vertex in self.graph:
            print(f"{vertex} --> {self.graph[vertex]}")

g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("E", "F")  
g.display()            


# ✅ Exact Definition of a Graph:
# A graph is a non-linear data structure consisting of a set of nodes (vertices) and edges (connections) between them.

# Formally, a graph is defined as:

# 👉 G = (V, E)
# V = Set of vertices (or nodes)

# E = Set of edges (pair of vertices that represent a connection)

# 🧠 Breakdown:
#   Term	                Meaning
# Vertex (V)	A point or node (like A, B, C...)
# Edge (E)   	A link/line between two vertices
# Undirected	A↔B (both ways)
# Directed	    A→B (one way only)
# Weighted	    Each edge has a value (e.g., distance or cost)
# Unweighted	All edges are equal

# ✅ Types of Graphs
# Type	Example Description
# Undirected Graph	A — B (no direction, mutual link)
# Directed Graph (Digraph)	A → B (one-way connection)
# Weighted Graph	A —(5)— B (edge has a weight of 5)
# Cyclic Graph	Has cycles (A → B → C → A)
# Acyclic Graph	No cycles (like a tree or DAG)
# Connected Graph	Every node is reachable
# Disconnected Graph	Some nodes are isolated

# 📍 Real-Life Examples:
# Real-world Example	Graph Nodes	Graph Edges
# Google Maps	Cities	Roads (with distances)
# Instagram	Users	Follows (edges)
# Web Browser	Web pages	Links between them
# Network Devices	Routers	Physical/virtual connections


# nothing much 