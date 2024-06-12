#------------dijkstra-----
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_vertex = None
        for vertex in graph:
            if vertex not in visited:
                if min_vertex is None or distances[vertex] < distances[min_vertex]:
                    min_vertex = vertex

        if min_vertex is None:
            break

        for neighbor, weight in graph[min_vertex].items():
            if neighbor not in visited:
                new_distance = distances[min_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        visited.add(min_vertex)
    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print(distances)