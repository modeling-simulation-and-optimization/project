from dataclasses import dataclass
import time
import random
import pygad


@dataclass
class Matrix:
    size_x: int
    size_y: int
    matrix: list[list] = None

    def __post_init__(self):
        if self.matrix is None:
            self.matrix = [[999] * self.size_x for _ in range(self.size_y)]

    def insert(self, x, y, value):
        self.matrix[x][y] = value


store_delivery_costs = [12, 10, 15]

selected_products = [1, 3]

product_costs = Matrix(3, 3)

product_costs.insert(0, 0, 7)
product_costs.insert(0, 1, 13)
product_costs.insert(0, 2, 10)

product_costs.insert(1, 0, 6)
product_costs.insert(1, 1, 4)
product_costs.insert(1, 2, 6)

product_costs.insert(2, 0, 15)
product_costs.insert(2, 1, 10)
product_costs.insert(2, 2, 9)


def fitness(solution, solution_idx):

    if (len(selected_products) != len(solution)):
        for i in range(len(solution)):
            if i+1 not in selected_products:
                solution[i] = 0
    total_cost = 0
    for i in range(len(solution)):
        if solution[i] != 0 and i+1 in selected_products:
            total_cost += product_costs.matrix[i][solution[i]-1]

    stores = list(set(solution))
    for i in range(len(stores)):
        if stores[i] != 0:
            total_cost += store_delivery_costs[stores[i]-1]

    return -total_cost


t1 = time.time()


ga_instance = pygad.GA(
    num_generations=250,
    num_parents_mating=3,
    fitness_func=fitness,
    gene_type=int,
    allow_duplicate_genes=True,
    num_genes=5,
    initial_population=[[random.randint(1, 3) for _ in range(3)] for _ in range(3)],
    mutation_percent_genes=0.01,
    mutation_type="random",
    mutation_num_genes=3,
    mutation_by_replacement=True,
    random_mutation_min_val=1,
    random_mutation_max_val=3
)

ga_instance.run()
t2 = time.time()

if ga_instance.best_solution_generation != -1:
    print(f"Best fitness value reached after {ga_instance.best_solution_generation} generations.\n")

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Minimum cost found: {abs(solution_fitness)}")
print(f"Time taken: {t2-t1}")
print(f"Solution: {solution}")

ga_instance.plot_fitness()
