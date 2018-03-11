#!/usr/bin/python3
"""
@author - Rahul Goswami

run as:
python3 bankers-algo.py

Output:

Enter the number of processes (n): 5
Enter the number of resources (m): 3

Enter the total available instances of each of the resources (space separated):
10 5 7

Enter the maximum resources (space separated) for each process: 
Process A : 7 5 3
Process B : 3 2 2
Process C : 9 0 2
Process D : 2 2 2
Process E : 4 3 3

Enter the allocated resources (space separated) for each process: 
Process A : 0 1 0
Process B : 2 0 0
Process C : 3 0 2
Process D : 2 1 1
Process E : 0 0 2
Available =  [3, 3, 2]
Maximum   =  [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
Allocated =  [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
Need      =  [[7, 4, 3], [1, 2, 2], [6, 0, 0], [0, 1, 1], [4, 3, 1]]

The system is safe...
The safe order is:  ['B', 'D', 'E', 'A', 'C']

"""
import string


def bankers_algo():
    """Find if system is safe or not using Banker's algorithm."""

    letters = string.ascii_uppercase

    n = int(input("Enter the number of processes (n): "))
    m = int(input("Enter the number of resources (m): "))

    print("\nEnter the total available instances of each of the resources (space separated):")
    avail = list(map(int, input().split()))
    assert len(avail) == m, "Please enter %d values" % m

    maximum = []
    print("\nEnter the maximum resources (space separated) for each process: ")
    for i in range(n):
        p = list(map(int, input("Process "+letters[i]+" : ").split()))
        assert len(p) == m, "Please enter %d values" % m
        maximum.append(p)

    alloc = []
    print("\nEnter the allocated resources (space separated) for each process: ")
    for i in range(n):
        p = list(map(int, input("Process " + letters[i] + " : ").split()))
        assert len(p) == m, "Please enter %d values" % m
        alloc.append(p)
        avail = [avail[i] - p[i] for i in range(m)]

    assert all(a >= 0 for a in avail), "Allocated more than total resources."

    need = []
    for i in range(n):
        p = [maximum[i][j] - alloc[i][j] for j in range(m)]
        need.append(p)

    print("Available = ", avail)
    print("Maximum   = ", maximum)
    print("Allocated = ", alloc)
    print("Need      = ", need)

    finished = [False for _ in range(n)]
    safe_order = []

    while not all(finished):

        found_any = False

        for p in range(n):
            if not finished[p] and all(need[p][r] <= avail[r] for r in range(m)):

                    avail = [avail[r] + alloc[p][r] for r in range(m)]
                    finished[p] = True
                    found_any = True
                    safe_order.append(letters[p])

        if not found_any:
            return None

    return safe_order


if __name__ == '__main__':

    safe_order = bankers_algo()
    if safe_order:
        print("\nThe system is safe...")
        print("The safe order is: ", safe_order)
    else:
        print("\nThe system is not safe...")
