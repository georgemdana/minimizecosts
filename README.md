### Dynamic Workers Cost Minimization
#### Overview
This Python script, dmg, is designed to minimize costs dynamically by optimizing worker-to-task assignments. It uses the OR-Tools library to solve a linear programming problem, ensuring each task is assigned to exactly one worker while minimizing the total cost based on randomly generated worker-task cost data.

#### Purpose
Clean Data: Generates random cost data for worker-task assignments.
Choose Best Model: Uses a Mixed Integer Programming (MIP) solver (SCIP) to find the optimal assignment of workers to tasks that minimizes total cost.

#### Features
Generates random cost matrices for a specified number of workers and tasks.
Assigns each task to exactly one worker and each worker to at most one task.
Calculates and displays the total cost of assignments and the time taken to compute the solution.
Supports testing with varying numbers of workers (5 to 9 in the provided script).

#### Dependencies
Python 3.x
ortools (Google OR-Tools for linear programming)
numpy (for generating test ranges)
random (for generating random cost data)
datetime (for measuring execution time)

Install dependencies using:
pip install ortools numpy

#### Usage
Run the script directly:python main.py

#### The script will:
Generate random cost data for 5 tasks and a varying number of workers (5 to 9).
Solve the assignment problem for each worker count.
Output the optimal worker-task assignments, total cost, and execution time for each run.

#### Script Details

Function: dynamicworkers(howmany)
Input: Number of workers (howmany)
Generates a cost matrix with random integers (0-100) for howmany workers and 5 tasks.
Uses OR-Tools' SCIP solver to minimize the total cost of task assignments.
Constraints:
Each worker is assigned to at most one task.
Each task is assigned to exactly one worker.

#### Outputs:
Total cost of the optimal assignment.
Worker-task assignments with individual costs.
Execution time for each run.
