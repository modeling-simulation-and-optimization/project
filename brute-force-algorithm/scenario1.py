from permutation import main, Matrix

# Define desired products
selected_products = [1, 3]

# Define cost of product in all stores
product_costs = Matrix(3, 3)
# Set cost of product A
product_costs.insert(0, 0, 7)
product_costs.insert(0, 1, 13)
product_costs.insert(0, 2, 10)
# Set cost of product B
product_costs.insert(1, 0, 6)
product_costs.insert(1, 1, 4)
product_costs.insert(1, 2, 6)
# Set cost of product C
product_costs.insert(2, 0, 15)
product_costs.insert(2, 1, 10)
product_costs.insert(2, 2, 9)

# Define delivery costs of stores
store_delivery_costs = [12, 10, 15]

# List of permutations
perm_array = [1, 2, 3]

main(store_delivery_costs, selected_products, product_costs, perm_array)
