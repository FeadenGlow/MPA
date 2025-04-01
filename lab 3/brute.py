import itertools

def brute_force_tsp(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(1, n))
    
    best_cost = float('inf')
    best_route = []

    for route in itertools.permutations(cities):
        current_cost = 0
        current_cost += distance_matrix[0][route[0]]  
        for i in range(len(route) - 1):
            current_cost += distance_matrix[route[i]][route[i + 1]]
        current_cost += distance_matrix[route[-1]][0] 

        if current_cost < best_cost:
            best_cost = current_cost
            best_route = (0,) + route + (0,)

    return best_route, best_cost


def test_brute():
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    route, cost = brute_force_tsp(distance_matrix)
    
    print("Оптимальний маршрут:", " → ".join(str(i+1) for i in route))
    print("Загальна довжина:", cost)

test_brute()