"""
Depth First Search
source : https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
O(V + E) time 
"""

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()

def depth_first_search(visited, graph, node):
    """
    >>> depth_first_search(visited, graph, 'A')
    A
    B
    D
    E
    F
    C
    """
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            depth_first_search(visited, graph, neighbor)


if __name__ == "__main__":
    import doctest
    doctest.testmod()