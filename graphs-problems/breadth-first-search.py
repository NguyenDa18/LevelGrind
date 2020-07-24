"""
Breadth First Search
source : https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
O(V + E) time 
"""

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []
queue = []

def breadth_first_search(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end = " ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)