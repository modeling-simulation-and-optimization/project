from itertools import product, groupby
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


arreglo = [1,2,3,4,5,6]

store_costs = [10, 15, 15, 10, 10, 15]
selected_products = [1, 2, 3, 4, 5]

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

permutations = [list(p) for p in product(arreglo, repeat=len(arreglo))]

if len(selected_products) < len(permutations[0]):
    for i in range(len(permutations[0])):
        if i+1 not in selected_products:
            for p in permutations:
                p[i] = 0

    permutations.sort()

    permutations = list(k for k,_ in groupby(permutations))

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
