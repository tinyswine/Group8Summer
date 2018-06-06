#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 17:17:29 2018

@author: paul
"""

import cvxpy as cp

if __name__ == "__main__":
    n = 6
    m = 3
    X = cp.Variable(n,1)
    Z = cp.Variable(n,1)
    Y = cp.Variable(m,1)
    
    objective = cp.Maximize(Z[5])
    
    constraints = []
    constraints += [X[0] + Y[0] - Z[0] == 150]
    constraints += [X[1] + Y[1] - 1.01 * X[0] + 1.003 * Z[0] - Z[1] == 100]
    constraints += [X[2] + Y[2] - 1.01 * X[1] + 1.003 * Z[1] - Z[2] == -200]
    constraints += [X[3] - 1.02 * Y[0] - 1.01 * X[2] + 1.003 * Z[2] - Z[3] == 200]
    constraints += [X[4] - 1.02 * Y[1] - 1.01 * X[3] + 1.003 * Z[3] - Z[4] == -50]
    constraints += [-1.02 * Y[2] - 1.01 * X[4] + 1.003 * Z[4] - Z[5] == -300]
    constraints += [X >= 0]
    constraints += [X <= 100]
    constraints += [Y >= 0]
    constraints += [Z >= 0]
    
    prob = cp.Problem(objective, constraints)
    
    result = prob.solve()