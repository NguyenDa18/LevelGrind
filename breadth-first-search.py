"""
https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
Breadth First Search
"""

def bfs_1(graph, node):
    """
    >>> bfs
    """
    visited = [node]
    queue = [node]

    while queue:
        vertex = queue.pop(0)
        print(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

bfs_1(graph, 'A')
