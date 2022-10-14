import numpy as np


def compute_solution(a, b):
    return np.linalg.inv(a).dot(b)
