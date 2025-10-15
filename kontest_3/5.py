import numpy as np

# Читаем размеры матрицы
k, m = map(int, input().split())

# Читаем матрицу
matrix = []
for _ in range(k):
    row = list(map(float, input().split()))
    matrix.append(row)

# Преобразуем в массив NumPy
matrix = np.array(matrix)

# Вычисляем нормы для каждой строки (длины векторов)
norms = np.linalg.norm(matrix, axis=1, keepdims=True)

# Нормируем каждую строку на её длину
normalized_matrix = matrix / norms

# Округляем до 2 знаков после запятой
normalized_matrix = np.round(normalized_matrix, 2)

# Выводим результат
for i in range(k):
    print(' '.join(map(str, normalized_matrix[i])))