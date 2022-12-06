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


def main(sdc, sp, pc, perm_array):
    store_delivery_costs, selected_products, product_costs = sdc, sp, pc
    permutations = [list(p) for p in product(perm_array, repeat=len(perm_array))]
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
                total_cost += store_delivery_costs[stores[i]-1]

        costs.append(total_cost)
    t2 = time.time()

    minimum = min(costs)
    index = costs.index(minimum)
    permutation = permutations[index]
    print(f"Minimum cost: {minimum}")
    print(f"Time: {t2-t1}")
    print(f"Permutation: {permutation}")
