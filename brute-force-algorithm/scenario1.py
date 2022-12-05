from itertools import product
from dataclasses import dataclass
import time

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


arreglo = [1,2,3]

store_costs = [12, 10, 15]

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


permutations = [list(p) for p in product(arreglo, repeat=len(arreglo))]


costs = list()

t1 = time.time()

for permutation in permutations:
    if (len(selected_products) != len(permutation)):
        for i in range(len(permutation)):
            if i+1 not in selected_products:
                permutation[i] = 0
    total_cost = 0
    for i in range(len(permutation)):
        if permutation[i] != 0 and i+1 in selected_products:
            total_cost += product_costs.matrix[i][permutation[i]-1]

    stores = list(set(permutation))
    for i in range(len(stores)):
        if stores[i] != 0:
            total_cost += store_costs[stores[i]-1]

    costs.append(total_cost)

t2 = time.time()
minimum = min(costs)
index = costs.index(minimum)
permutation = permutations[index]
print(f"Minimum cost: {minimum}")
print(f"Time: {t2-t1}")
print(f"Permutation: {permutation}")