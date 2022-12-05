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


store_costs = [10, 15, 15, 10, 10, 15]

selected_products = [1,2,3,4,5]

product_costs = Matrix(6, 5)
product_costs.insert(0, 0, 18)
product_costs.insert(0, 1, 24)
product_costs.insert(0, 2, 22)
product_costs.insert(0, 3, 28)
product_costs.insert(0, 4, 24)
product_costs.insert(0, 5, 27)

product_costs.insert(1, 0, 39)
product_costs.insert(1, 1, 45)
product_costs.insert(1, 2, 45)
product_costs.insert(1, 3, 47)
product_costs.insert(1, 4, 42)
product_costs.insert(1, 5, 48)

product_costs.insert(2, 0, 29)
product_costs.insert(2, 1, 23)
product_costs.insert(2, 2, 23)
product_costs.insert(2, 3, 17)
product_costs.insert(2, 4, 24)
product_costs.insert(2, 5, 20)

product_costs.insert(3, 0, 48)
product_costs.insert(3, 1, 54)
product_costs.insert(3, 2, 53)
product_costs.insert(3, 3, 57)
product_costs.insert(3, 4, 47)
product_costs.insert(3, 5, 55)

product_costs.insert(4, 0, 59)
product_costs.insert(4, 1, 44)
product_costs.insert(4, 2, 53)
product_costs.insert(4, 3, 47)
product_costs.insert(4, 4, 59)
product_costs.insert(4, 5, 53)


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
            total_cost += store_costs[stores[i]-1]

    return -total_cost

t1 = time.time()


ga_instance = pygad.GA(num_generations=500,
                    num_parents_mating=5,
                    fitness_func=fitness,
                    gene_type=int,
                    allow_duplicate_genes=True,
                    num_genes=5,
                    initial_population=[[random.randint(1,6) for _ in range(5)] for _ in range(5)],
                    mutation_percent_genes=0.01,
                    mutation_type="random",
                    mutation_num_genes=3,
                    mutation_by_replacement=True,
                    random_mutation_min_val=1,
                    random_mutation_max_val=6)

ga_instance.run()
t2 = time.time()

best_sol = ga_instance.best_solution()

print(f"Minimum cost found: {abs(best_sol[1])}")
print(f"Time taken: {t2-t1}")
print(f"Solution: {best_sol[0]}")