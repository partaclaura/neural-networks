

def minors(matrix):
    m = []
    # for each row and column
    for i in range(len(matrix)):
        m_row = []
        for j in range(len(matrix)):
            # extract the minor corresponding to the row and column
            # and compute the determinant
            m_row.append(compute_det(extract_minor(matrix, j, i)))
        m.append(m_row)
    return m


def cofactors(matrix):
    c = []
    # for each cell, check if alternate and if true then change sign
    for i in range(len(matrix)):
        c_row = []
        for j in range(len(matrix)):
            if (i + j) % 2:
                # alternate cell
                c_row.append(matrix[i][j] * (-1))
            else:
                c_row.append(matrix[i][j])
        c.append(c_row)
    return c


def adjugate(matrix):
    return cofactors(minors(matrix))


def transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix))]


def extract_minor(matrix, i, j):
    # one liner to return a matrix which excludes the i row and  j column
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def compute_det(matrix):
    d = 0
    # last recursive call -> quick compute
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        # get submatrix for each colum and sum all returns from recursion
        for i in range(len(matrix)):
            submatrix = compute_det(extract_minor(matrix, 0, i))
            d += ((-1) ** i) * matrix[0][i] * submatrix
        return d


def inverse(matrix):
    if compute_det(matrix) == 0:
        return

    # transpose -> minors -> cofact -> adj
    a_star = adjugate(transpose(matrix))

    determinant = compute_det(matrix)
    inv = []
    for i in range(len(matrix)):
        inv_row = []
        for j in range(len(matrix)):
            inv_row.append(a_star[j][i] / determinant)
        inv.append(inv_row)
    return inv


# scalar product
def compute_product(a, b):
    sol = []
    for i in range(len(a)):
        s = 0
        for j in range(len(b)):
            s += b[j] * a[i][j]
        sol.append(s)
    return sol


# A * X = B; X = A^(-1) * B
def compute_solution(a,  b):
    return compute_product(inverse(a), b)\
