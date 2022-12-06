from genetic import main, Matrix
import random

# Define desired products
selected_products = [1, 2, 3, 4, 5]

# Define cost of product in all stores
product_costs = Matrix(6, 5)
# Set cost of product A
product_costs.insert(0, 0, 18)
product_costs.insert(0, 1, 24)
product_costs.insert(0, 2, 22)
product_costs.insert(0, 3, 28)
product_costs.insert(0, 4, 24)
product_costs.insert(0, 5, 27)
# Set cost of product B
product_costs.insert(1, 0, 39)
product_costs.insert(1, 1, 45)
product_costs.insert(1, 2, 45)
product_costs.insert(1, 3, 47)
product_costs.insert(1, 4, 42)
product_costs.insert(1, 5, 48)
# Set cost of product C
product_costs.insert(2, 0, 29)
product_costs.insert(2, 1, 23)
product_costs.insert(2, 2, 23)
product_costs.insert(2, 3, 17)
product_costs.insert(2, 4, 24)
product_costs.insert(2, 5, 20)
# Set cost of product D
product_costs.insert(3, 0, 48)
product_costs.insert(3, 1, 54)
product_costs.insert(3, 2, 53)
product_costs.insert(3, 3, 57)
product_costs.insert(3, 4, 47)
product_costs.insert(3, 5, 55)
# Set cost of product E
product_costs.insert(4, 0, 59)
product_costs.insert(4, 1, 44)
product_costs.insert(4, 2, 53)
product_costs.insert(4, 3, 47)
product_costs.insert(4, 4, 59)
product_costs.insert(4, 5, 53)

# Define delivery costs of stores
store_delivery_costs = [10, 15, 15, 10, 10, 15]

# Define num_generations, num_parents_mating, initial_population, random_mutation_min_val, random_mutation_max_val
genetic_params = [
    500, 5, [[random.randint(1, 6) for _ in range(5)] for _ in range(5)], 1, 6
]

main(store_delivery_costs, selected_products, product_costs, genetic_params)
