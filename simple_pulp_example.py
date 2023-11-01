import pulp

# Define variables
x = pulp.LpVariable("x", 0, 3)
y = pulp.LpVariable("y", 0, 1)

# Define problem
prob = pulp.LpProblem("myProblem", pulp.LpMinimize)
# Add constriants
prob += x + y <= 2
# Add OF
prob += -4*x + y

# Solve with default included solver
status = prob.solve()
# Try another solver
# status = prob.solve(pulp.GLPK(msg = 0))

# Print info
print(f"Status {pulp.LpStatus[status]}({status}), with x={pulp.value(x)}, y={pulp.value(y)}")