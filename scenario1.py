"""
Escenario 1 Proyecto (Sencillo) - MOS
Realizado por:
Juan Andrés Romero C - 202013449
Juan Sebastián Alegría - 202011282
"""

from pyomo.environ import *
from pyomo.opt import SolverFactory

model = ConcreteModel()

# Sets and parameters
model.P = RangeSet(1, 3)  # Products
model.L = RangeSet(1, 3)  # Stores

# Products wanted by the buyer
model.N = Set(within=model.P, initialize=[1,3])

model.Costs = Param(model.P, model.L, mutable=True)
model.DeliveryCosts = Param(model.L, mutable=True)

# Costs of each product in each store
model.Costs[1, 1] = 7
model.Costs[1, 2] = 13
model.Costs[1, 3] = 10

model.Costs[2, 1] = 6
model.Costs[2, 2] = 4
model.Costs[2, 3] = 6

model.Costs[3, 1] = 15
model.Costs[3, 2] = 10
model.Costs[3, 3] = 9

# Delivery costs per store
model.DeliveryCosts[1] = 12
model.DeliveryCosts[2] = 10
model.DeliveryCosts[3] = 15

# Variables
model.x = Var(model.P, model.L, domain=Binary)  # Product selected
model.y = Var(model.L, domain=Binary)  # Purchase in shop

"""
Objective function
The objective function seeks to minimize the sum of the costs of the chosen products for all stores.
If a store has at least one product chosen, the binary variable Yl will allow us to
include to the final sum of the shipping cost corresponding to that store.
"""
model.targetFunc = Objective(expr=sum(sum(
    model.Costs[j, l]*model.x[j, l] for j in model.P) + model.DeliveryCosts[l] * model.y[l] for l in model.L), sense=minimize)


# Constraints
def activate_y_if_l_is_chosen(model, l):
    """
    This restriction indicates that if at least one product is chosen from a store l,
    the variable Y must be activated, since it means that a purchase
    is being made in store l.
    """
    return sum(model.x[j, l] - len(model.P)*model.y[l] for j in model.P) <= 0


def wanted_products_must_be_bought(model, j):
    """
    This restriction indicates that for each available product that the buyer wants,
    exactly 1 of them must be purchased. That is, it is not possible to buy more than
    one specific product per store.
    """
    return sum(model.x[j, l] for l in model.L) == 1


model.activate_y = Constraint(model.L, rule=activate_y_if_l_is_chosen)
model.wanted_products = Constraint(model.N, rule=wanted_products_must_be_bought)

# Applying the solver
SolverFactory('glpk').solve(model)
model.display()
