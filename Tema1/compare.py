import normal_solution
import numpy_solution
import parse


if __name__ == '__main__':
    file_input = open('lin_eq.txt', 'r')
    lines = file_input.readlines()
    m_coef, m_const = parse.parse_input(lines)
    sol1 = normal_solution.compute_solution(m_coef, m_const)
    print("Solution without using NumPy: ")
    print(sol1)
    print("Solution using NumPy: ")
    sol2 = numpy_solution.compute_solution(m_coef, m_const)
    print(sol2)

    corresp = True
    for i in range(len(sol1)):
        if sol1[i] != sol2[i]:
            corresp = False
    if corresp:
        print("Values do not correspond.")
    else:
        print("Values correspond.")
