"""
Bono Entrega 2 - MOS
Realizado por:
Juan Andrés Romero C - 202013449
Juan Sebastián Alegría - 202011282
"""

from pyomo.environ import *
from pyomo.opt import SolverFactory

model = ConcreteModel()

model.P = RangeSet(1, 5)
model.L = RangeSet(1, 6)
model.N = Set(within=model.P, initialize=[1, 2, 3, 4, 5])

model.Costs = Param(model.P, model.L, mutable=True)
model.DeliveryCosts = Param(model.L, mutable=True)

# Costs of each product in each store
model.Costs[1,1] = 18
model.Costs[1,2] = 24
model.Costs[1,3] = 22
model.Costs[1,4] = 28
model.Costs[1,5] = 24
model.Costs[1,6] = 27

model.Costs[2,1] = 39
model.Costs[2,2] = 45
model.Costs[2,3] = 45
model.Costs[2,4] = 47
model.Costs[2,5] = 42
model.Costs[2,6] = 48

model.Costs[3,1] = 29
model.Costs[3,2] = 23
model.Costs[3,3] = 23
model.Costs[3,4] = 17
model.Costs[3,5] = 24
model.Costs[3,6] = 20

model.Costs[4,1] = 48
model.Costs[4,2] = 54
model.Costs[4,3] = 53
model.Costs[4,4] = 57
model.Costs[4,5] = 47
model.Costs[4,6] = 55

model.Costs[5,1] = 59
model.Costs[5,2] = 44
model.Costs[5,3] = 53
model.Costs[5,4] = 47
model.Costs[5,5] = 59
model.Costs[5,6] = 53

# Delivery costs per store
model.DeliveryCosts[1] = 10
model.DeliveryCosts[2] = 15
model.DeliveryCosts[3] = 15
model.DeliveryCosts[4] = 10
model.DeliveryCosts[5] = 10
model.DeliveryCosts[6] = 15

model.x = Var(model.P, model.L, domain=Binary)
model.y = Var(model.L, domain=Binary)

model.targetFunc = Objective(expr=sum(sum(model.Costs[j,l] for j in model.P) + model.DeliveryCosts[l] * model.y[l] for l in model.L), sense=minimize)

def activate_y_if_l_is_chosen(model, l):
    return sum(model.x[j,l] - len(model.P) * model.y[l] for j in model.P) <= 0

def wanted_products_must_be_bought(model, j):
    return sum(model.x[j,l] for l in model.L) == 1

model.activate_y = Constraint(model.L, rule=activate_y_if_l_is_chosen)
model.wanted_products = Constraint(model.P, rule=wanted_products_must_be_bought)

SolverFactory('glpk').solve(model)
model.display()