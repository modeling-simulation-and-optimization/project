from dataclasses import dataclass
import time
import pygad

store_delivery_costs, selected_products, product_costs = [], [], None


@dataclass
class Matrix:
    size_x: int
    size_y: int
    matrix: list[list] = None

    def __post_init__(self):
        if self.matrix is None:
            self.matrix = [[999] * self.size_x for _ in range(self.size_y)]

    def insert(self, product, store, cost):
        self.matrix[product][store] = cost


def set_param_values(sdc, sp, pc):
    global store_delivery_costs
    global selected_products
    global product_costs
    store_delivery_costs, selected_products, product_costs = sdc, sp, pc


def fitness(solution, solution_idx):
    if (len(selected_products) != len(solution)):
        for i in range(len(solution)):
            if i+1 not in selected_products:
                solution[i] = 0

    total_cost = 0

    for i in range(len(solution)):
        selected_store = solution[i]
        if selected_store != 0 and i+1 in selected_products:
            total_cost += product_costs.matrix[i][selected_store-1]

    stores = list(set(solution))
    for i in range(len(stores)):
        store = stores[i]
        if store != 0:
            total_cost += store_delivery_costs[store-1]
    return -total_cost


def main(sdc, sp, pc, g_params):
    set_param_values(sdc, sp, pc)

    ga_instance = pygad.GA(
        num_generations=g_params[0],
        num_parents_mating=g_params[1],
        fitness_func=fitness,
        gene_type=int,
        allow_duplicate_genes=True,
        num_genes=5,
        initial_population=g_params[2],
        mutation_percent_genes=0.01,
        mutation_type="random",
        mutation_num_genes=3,
        mutation_by_replacement=True,
        random_mutation_min_val=g_params[3],
        random_mutation_max_val=g_params[4]
    )

    t1 = time.time()
    ga_instance.run()
    t2 = time.time()

    if ga_instance.best_solution_generation != -1:
        print(f"Best fitness value reached after {ga_instance.best_solution_generation} generations.")

    solution, solution_fitness, _ = ga_instance.best_solution()
    print(f"Minimum cost found: {abs(solution_fitness)}")
    print(f"Time taken: {t2-t1}")
    print(f"Solution: {solution}")

    ga_instance.plot_fitness()
