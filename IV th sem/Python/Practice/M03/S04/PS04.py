'''
Write a Python program to check if duplicate values exist in a list.
'''
def has_duplicates(lst):
    return len(lst) != len(set(lst))

l=list(map(int,input("Enter numbers separated by space: ").split()))
print(has_duplicates(l))

"""
optimization_problems_demo.py

Demonstrates basic optimization problems using Python:
1. Linear Programming (Scipy)
2. Unconstrained Optimization
3. Knapsack Problem (Greedy Approximation)
"""

import numpy as np
from scipy.optimize import linprog, minimize


# 1. Linear Programming Example
def linear_programming():
    # Maximize: 3x + 5y
    # Subject to:
    # 2x + y <= 20
    # x + 3y <= 30
    # x, y >= 0

    c = [-3, -5]
    A = [[2, 1], [1, 3]]
    b = [20, 30]

    result = linprog(c, A_ub=A, b_ub=b, method='highs')

    print("Linear Programming Result:")
    print("Optimal value:", -result.fun)
    print("x =", result.x[0], "y =", result.x[1])
    print()


# 2. Unconstrained Optimization Example
def unconstrained_optimization():
    # Minimize: f(x) = (x - 3)^2 + 4

    def f(x):
        return (x - 3) ** 2 + 4

    result = minimize(f, x0=0)

    print("Unconstrained Optimization Result:")
    print("Minimum value:", result.fun)
    print("x =", result.x[0])
    print()


# 3. Knapsack Problem (Greedy Approximation)
def knapsack():
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    items = list(zip(values, weights))
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    remaining = capacity

    for value, weight in items:
        if weight <= remaining:
            total_value += value
            remaining -= weight

    print("Knapsack (Greedy Approximation) Result:")
    print("Maximum value:", total_value)
    print()


if __name__ == "__main__":
    linear_programming()
    unconstrained_optimization()
    knapsack()