import numpy as np
from scipy.optimize import linprog


def solve_transportation_problem(cost_matrix, supply, demand):
    """
    Solves the transportation problem using linear programming.

    Parameters:
        cost_matrix (2D list or numpy array): The cost of transporting from each supply to each demand.
        supply (list): Available supply at each source.
        demand (list): Required demand at each destination.

    Returns:
        float: The optimal transportation cost.
        dict: The detailed transportation plan.
    """
    # Convert inputs to numpy arrays for easier manipulation
    cost_matrix = np.array(cost_matrix)
    supply = np.array(supply)
    demand = np.array(demand)

    # Get dimensions
    num_sources, num_destinations = cost_matrix.shape

    # Flatten the cost matrix for the linear programming model
    c = cost_matrix.flatten()

    # Create the equality constraint matrix
    A_eq = np.zeros((num_sources + num_destinations, num_sources * num_destinations))

    # Supply constraints
    for i in range(num_sources):
        A_eq[i, i * num_destinations:(i + 1) * num_destinations] = 1

    # Demand constraints
    for j in range(num_destinations):
        A_eq[num_sources + j, j::num_destinations] = 1

    # Concatenate supply and demand to form the b_eq vector
    b_eq = np.concatenate([supply, demand])

    # Set bounds for variables (non-negative)
    bounds = [(0, None) for _ in range(num_sources * num_destinations)]

    # Solve the linear programming problem
    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    # Check if the problem has a solution
    if result.success:
        # Reshape the solution to match the cost matrix dimensions
        transportation_plan = result.x.reshape(num_sources, num_destinations)
        return result.fun, transportation_plan
    else:
        raise ValueError("The transportation problem could not be solved.")


# Example usage
cost_matrix = [
    [8,7,8,10,7,7,8,9],
    [6,5,10,8,7,9,6,7],
    [5,10,8,9,10,5,7,9],
    [9,9,7,9,6,5,8,7]
]
supply = [12, 5 ,3, 4]
demand = [2,2,1,3,6,3,6,1]

# Solve the problem
optimal_cost, transportation_plan = solve_transportation_problem(cost_matrix, supply, demand)

# Print results
print("Optimal Transportation Cost:", optimal_cost)
print("Transportation Plan:")
print(transportation_plan)