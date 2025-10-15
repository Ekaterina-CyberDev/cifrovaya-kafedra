import numpy as np

# Читаем первую строку с размерами матрицы и значением target
n, m, target = map(int, input().split())

# Читаем матрицу
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Преобразуем в массив NumPy
matrix = np.array(matrix)

# Находим четные элементы и заменяем их на target
# Элемент четный, если остаток от деления на 2 равен 0
matrix[matrix % 2 == 0] = target

# Выводим результат
for i in range(n):
    print(' '.join(map(str, matrix[i])))