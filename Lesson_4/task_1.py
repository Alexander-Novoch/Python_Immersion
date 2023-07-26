# Напишите функцию для транспонирования матрицы

orig_matrix = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]


def transpose_matrix(matrix):
    tran_matrix = [[0 for j in range(len(matrix))] for i in
                   range(len(matrix[0]))]  # создание матрицы такого же размера, заполненой "0"
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tran_matrix[j][i] = matrix[i][j]
    return tran_matrix


print(orig_matrix)
print(transpose_matrix(orig_matrix))
