# 🔁 Whole concept in a real-world analogy

# Imagine a rescue operation 🚁
# You rescue person A first.
# Then you find A’s friends: B and C.
# You put B and C in a queue (you’ll rescue them next).
# Then you go to B, then to C, then to their friends (if any).
# That’s BFS. You rescue by levels — not by diving deep.


def dfs(graph, node, visited):
    visited.add(node)
    print(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A"],
    "D": ["B"],
    "E": ["B"]
}

visited = set()
dfs(graph, "A", visited)

# ✅ Time Complexity: O(V + E)
# ✅ Space Complexity: O(V)