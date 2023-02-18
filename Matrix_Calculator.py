"""  Matrix - Calculator  """

def print_matrix(matrix):
    for row in matrix:
        print(row)

def add_matrices(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        print('\nError, matrices have different dimensions')
        return None
    result_matrix = []
    for i in range(len(matrix_1)):
        row = []
        for j in range(len(matrix_1[0])):
            row.append(matrix_1[i][j] + matrix_2[i][j])
        result_matrix.append(row)
    return result_matrix

def subtract_matrices(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        print('\nError, matrices have different dimensions')
        return None
    result_matrix = []
    for i in range(len(matrix_1)):
        row = []
        for j in range(len(matrix_1[0])):
            row.append(matrix_1[i][j] - matrix_2[i][j])
        result_matrix.append(row)
    return result_matrix

def multiply_by_constant(matrix, k):
    result_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            value = k * matrix[i][j]
            row.append(value)
        result_matrix.append(row)
    return result_matrix
            
def multipy_matrices(matrix_1, matrix_2):
    if len(matrix_1[0]) == len(matrix_2):
        result_matrix = []
        for i in range(len(matrix_1)):
            row = []
            for j in range(len(matrix_2[0])):
                sum = 0
                for k in range(len(matrix_2)):
                    sum += matrix_1[i][k] * matrix_2[k][j]
                row.append(sum)
            result_matrix.append(row)
        return result_matrix
    else:
        return("Error, multiplication can not be implemented, check your matrices's dimensions")

def transpose_matrix(matrix):
    trans = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        trans.append(row)
    return trans

def find_rank(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(i + 1, len(matrix)):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
            else:
                continue
        factor = matrix[i][i]
        for j in range(len(matrix[i])):
            matrix[i][j] /= factor
        for j in range(i + 1, len(matrix)):
            factor = matrix[j][i]
            for k in range(len(matrix[j])):
                matrix[j][k] -= factor * matrix[i][k]
    rank = 0
    for row in matrix:
        if any(row):
            rank += 1
    return rank

def determinant(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        raise ValueError("Matrix must be square")
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for j in range(n):
        sign = (-1)**j
        submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        subdet = determinant(submatrix)
        det += sign * matrix[0][j] * subdet
    return det

def minor_matrix(matrix, row, col):
    result_matrix = []
    for i in range(len(matrix)):
        if i == row:
            continue
        new_row = []
        for j in range(len(matrix)):
            if j == col:
                continue
            new_row.append(matrix[i][j])
        result_matrix.append(new_row)
    return result_matrix

def reverse(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        raise ValueError("Matrix must be square")
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is not invertible")
    cofactors = []
    for i in range(n):
        row = []
        for j in range(n):
            sign = (-1)**(i+j)
            minor = minor_matrix(matrix, i, j)
            minor_det = determinant(minor)
            cofactor = sign * minor_det
            row.append(cofactor)
        cofactors.append(row)
    transposed = transpose_matrix(cofactors)
    inverse = multiply_by_constant(transposed, 1/det)
    return inverse

def prompt_for_matrices():
    rows_1 = int(input("\nEnter the number of rows in the first matrix - A: "))
    cols_1 = int(input("\nEnter the number of columns in the first matrix - A : "))
    print("\nEnter the elements of the first matrix - A, row by row:")
    matrix_1 = []
    for i in range(rows_1):
        row = []
        for j in range(cols_1):
            element = float(input(f"\nEnter element A({i+1}, {j+1}) of the first matrix: "))
            row.append(element)
        matrix_1.append(row)
    print('\n You entered the (first) matrix A: \n')
    print_matrix(matrix_1)
    rows_2 = int(input("\nEnter the number of rows in the second matrix - B: "))
    cols_2 = int(input("\nEnter the number of columns in the second matrix - B: "))
    print("\nEnter the elements of the second matrix - B, row by row:")
    matrix_2 = []
    for i in range(rows_2):
        row = []
        for j in range(cols_2):
            element = float(input(f"\nEnter element B({i+1}, {j+1}) of the second matrix: "))
            row.append(element)
        matrix_2.append(row)
    print('\n You entered the (second) matrix B: \n')
    print_matrix(matrix_2)
    return matrix_1, matrix_2

def get_matrix():
    rows = int(input("\nEnter the number of rows in matrix A: "))
    cols = int(input("\nEnter the number of columns in matrix A: "))
    print("\nEnter the elements of the matrix, row by row:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"\nEnter element A({i+1}, {j+1}) of the matrix: "))
            row.append(element)
        matrix.append(row)
    print('\nYou entered the matrix A: \n')
    print_matrix(matrix)
    return matrix

def print_operations():
    print("\nOperations:\n")
    print("1. Add matrices\n")
    print("2. Subtract matrices\n")
    print("3. Multiply matrix by constant\n")
    print("4. Multiply matrices\n")
    print("5. Find transpose of matrix\n")
    print("6. Find rank of matrix\n")
    print("7. Find minor matrix\n")
    print("8. Find determinant of matrix\n")
    print("9. Find reversed matrix\n")
    print("0. Exit")

def main():
    while True:
        print_operations()
        choice = int((input('\n Select an operation (0-9): ')))
        if choice == 1:
            matrix_1, matrix_2 = prompt_for_matrices()
            sum = add_matrices(matrix_1, matrix_2)
            print('\nA + B = \n')
            print_matrix(sum)
        elif choice == 2:
            matrix_1, matrix_2 = prompt_for_matrices()
            sub = subtract_matrices(matrix_1, matrix_2)
            print('\nA - B = \n')
            print_matrix(sub)
        elif choice == 3:
            matrix = get_matrix()
            k = float(input('\nEnter the constant: '))
            print('\nA * '+str(k)+' = \n')
            print_matrix(multiply_by_constant(matrix, k))
        elif choice == 4:
            matrix_1, matrix_2 = prompt_for_matrices()
            mult = multipy_matrices(matrix_1, matrix_2)
            print('\nA * B = \n')
            print_matrix(mult)
        elif choice == 5:
            matrix = get_matrix()
            print('\nTraspose of A is \n')
            print_matrix(transpose_matrix(matrix))
        elif choice == 6:
            matrix = get_matrix()
            rank = find_rank(matrix)
            print('\nThe Rank of A is '+str(rank))
        elif choice == 7:
            matrix = get_matrix()
            row = int(input('\nEnter the number of the row that you want removed: '))
            col = int(input('\nEnter the number of the column that you want removed: '))
            print('\nThe minor matrix is \n')
            print_matrix(minor_matrix(matrix, row-1, col-1))
        elif choice == 8:
            matrix = get_matrix()
            print('\nDet(A) = '+ str(determinant(matrix)))
        elif choice == 9:
            matrix = get_matrix()
            reversed = reverse(matrix)
            print('\nInverse of A is \n')
            print_matrix(reversed)
        elif choice == 0:
            print('\n Bye Bye')
            break
        else:
            print('\nError. Please select an operation from 0 to 9\n')

if __name__ == "__main__":
    main()
