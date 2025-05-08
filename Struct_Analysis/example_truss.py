import numpy as np
import scipy.sparse as sp


def example1():
    """
    Example: 3-bar truss analysis in Python.
    """
    # Coordinates of 3 nodes
    X = np.array([[0.00, 0.00],
                  [0.00, 2.00],
                  [2.00, 0.00]])

    # Topology matrix (node1, node2, property index)
    IX = np.array([[1, 3, 1],
                   [1, 2, 1],
                   [2, 3, 1]])

    # Element property matrix [E A]
    mprop = np.array([[1.0, 1.0]])

    # Prescribed loads (node, ldof, force)
    loads = np.array([[3, 2, -10]])

    # Boundary conditions (node, ldof, displacement)
    bound = np.array([[1, 1, 0.0],
                      [1, 2, 0.0]])

    # Number of equations and elements
    plotdof = 6
    return X, IX, mprop, loads, bound, plotdof

def example2():
    """
    Example: 9-bar truss analysis in Python.
    """
    # Coordinates of 3 nodes (x, y)
    X = np.array([[0.00, 0.00],  # 1
                  [0.00, 2.00],  # 2
                  [2.00, 0.00],  # 3
                  [2.00, 2.00],  # 4
                  [4.00, 0.00],  # 5
                  [4.00, 2.00]])

    # Topology matrix (node1, node2, property index)
    IX = np.array([[1, 3, 1],
                   [1, 2, 1],
                   [2, 3, 1],
                   [2, 4, 1],
                   [3, 4, 1],
                   [3, 5, 1],
                   [4, 5, 1],
                   [4, 6, 1],
                   [5, 6, 1]
                   ])

    # Element property matrix [E A]
    mprop = np.array([[1.0, 1.0]])

    # Prescribed loads (node, ldof, force)
    loads = np.array([[4, 2, -10]])

    # Boundary conditions (node, ldof, displacement)
    bound = np.array([[1, 1, 0.0],
                      [1, 2, 0.0],
                      [2, 1, 0.0]])

    # Number of equations and elements
    plotdof = 6

    return X, IX, mprop, loads, bound, plotdof
