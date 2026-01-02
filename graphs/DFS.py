# 🔁 Whole concept in a real-world analogy

# Imagine a rescue operation 🚁
# You rescue person A first.
# Then you find A’s friends: B and C.
# You put B and C in a queue (you’ll rescue them next).
# Then you go to B, then to C, then to their friends (if any).
# That’s BFS. You rescue by levels — not by diving deep.


def dfs_recursion(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursion(graph, neighbor, visited)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs_recursion(graph, 'A')

######################################################################################################

def dfs_stack(graph,start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs_stack(graph, 'C')

