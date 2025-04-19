# dmg
#!/usr/bin/env python
# coding: utf-8

# In[24]:

# What: Minimize Costs Dynamically
# Who: Dana M George
# Purpose: 
#   clean data
#   choose best model

from ortools.linear_solver import pywraplp
from datetime import datetime
import numpy as np
import random
start = datetime.now()

def dynamicworkers(howmany):
    # Add workers 
    # Generate random number list for additional workers
    def add_workers(howmany, jobs):
        lists_master = []
        for i in range(howmany):
            sub_list = []
            for j in range(jobs):
                sub_list.append(random.randint(0, 100))
            lists_master.append(sub_list)
        return lists_master

    # Data - each row = 1 worker, each column = 1 time to complete 1 job
    costs = add_workers(howmany, 5)

    num_workers = len(costs)  # number of workers >= tasks
    num_tasks = len(costs[0])

    # Solver
    # Create the mip solver with the SCIP. Mixed integer programs (MIPs) with the CPLEX mixed integer optimizer; 
    # that is, solving models in which one or more variables must take integer solution values
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Assign Variables
    # x[i, j] is an array of 0-1 variables, which will be 1 if worker i is assigned to task j.
    x = {}
    for i in range(num_workers):
        for j in range(num_tasks):
            x[i, j] = solver.IntVar(0, 1, '')

    # Determine Constraints
    # Each worker is assigned to at most 1 task.
    for i in range(num_workers):
        solver.Add(solver.Sum([x[i, j] for j in range(num_tasks)]) <= 1) # only 1 worker / task

    # Each task is assigned to exactly one worker.
    for j in range(num_tasks):
        solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) == 1) # only 1 task / worker 

    # Define our Objective
    objective_terms = []
    for i in range(num_workers):
        for j in range(num_tasks):
            objective_terms.append(costs[i][j] * x[i, j]) # Algorithm to solve for minimum cost
    solver.Minimize(solver.Sum(objective_terms))

    # Solve the algorithm
    status = solver.Solve()

    # Print solution.
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print(" ")
        print("Algorithm with " + str(num_workers) + " workers")
        print('Total cost = ', solver.Objective().Value(), '\n')
        for i in range(num_workers):
            for j in range(num_tasks):
                # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
                if x[i, j].solution_value() > 0.5:
                    print('Worker %d assigned to task %d.  Cost = %d' %
                          (i, j, costs[i][j]))

    complete = datetime.now()
    time = complete - start
    print(" ")
    print("Time to Run for " + str(num_workers) + " workers")
    print(time)
    print("------------------------------------------------")


# In[25]:


workertest = np.arange(5, 10, 1).tolist()
for i in workertest:
    dynamicworkers(i)
