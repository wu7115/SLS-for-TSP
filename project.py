import math
import random

def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    num_cities = len(tour)

    for i in range(num_cities - 1):
        total_distance += distance_matrix[tour[i]][tour[i + 1]]

    total_distance += distance_matrix[tour[num_cities - 1]][tour[0]]  # Return to the starting city
    return total_distance

def simulated_annealing(tour, distance_matrix, temperature, cooling_rate, num_iterations):
    current_tour = tour.copy()
    current_distance = calculate_total_distance(current_tour, distance_matrix)

    for iteration in range(num_iterations):
        # Generate a new neighboring tour
        new_tour = current_tour.copy()
        index1, index2 = random.sample(range(len(new_tour)), 2)
        new_tour[index1], new_tour[index2] = new_tour[index2], new_tour[index1]
        # new_tour = sorted(current_tour, key=lambda x: random.random())

        # Calculate the new distance
        new_distance = calculate_total_distance(new_tour, distance_matrix)

        # Accept the new tour with a probability based on temperature and cost change
        if new_distance < current_distance or random.uniform(0, 1) < math.exp((current_distance - new_distance) / temperature):
            current_tour = new_tour
            current_distance = new_distance

        # Reduce temperature
        temperature *= 1 - cooling_rate

    return current_tour, current_distance

# Example Usage
num_cities = 5
distance_matrix = [[0, 2, 9, 10, 6],
                   [2, 0, 4, 5, 8],
                   [9, 4, 0, 7, 3],
                   [10, 5, 7, 0, 1],
                   [6, 8, 3, 1, 0]]

initial_tour = list(range(num_cities))
initial_temperature = 1000
cooling_rate = 0.005
num_iterations = 1000

final_tour, final_distance = simulated_annealing(initial_tour, distance_matrix, initial_temperature, cooling_rate, num_iterations)

print("Final Tour:", final_tour)
print("Final Distance:", final_distance)