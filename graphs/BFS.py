from collections import deque

def bfs(graph, start):
    visited = set()          # Keep track of visited nodes
    queue = deque([start])   # Create queue and add starting node
    visited.add(start)

    while queue:
        node = queue.popleft()   # Remove from front (FIFO)
        print(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A","F","G"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"],
    "G": ["C"]
}

bfs(graph, "A")

# ✅ Time Complexity: O(V + E)
# ✅ Space Complexity: O(V)