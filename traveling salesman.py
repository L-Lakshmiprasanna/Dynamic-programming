#-----------------Traveling sales man-------


def tsp_recursive(distance_matrix):
    n = len(distance_matrix)
    def all_cities_visited(visited):
        return len(visited) == n
    def tsp(visited, pos):
        if all_cities_visited(visited):
            return distance_matrix[pos][0]
        min_distance = float('inf')
        for city in range(n):
            if city not in visited:
                new_visited = visited + [city]
                new_distance = distance_matrix[pos][city] + tsp(new_visited, city)
                min_distance = min(min_distance, new_distance)

        return min_distance

    initial_visited = [0]
    return tsp(initial_visited, 0)
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_distance = tsp_recursive(distance_matrix)
print(f"Minimum distance: {min_distance}")