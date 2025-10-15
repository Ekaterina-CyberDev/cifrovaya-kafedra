import numpy as np

# Читаем размеры матриц
k, m = map(int, input().split())

# Читаем первую матрицу
matrix1 = []
for _ in range(k):
    row = list(map(float, input().split()))
    matrix1.append(row)

# Читаем вторую матрицу
matrix2 = []
for _ in range(k):
    row = list(map(float, input().split()))
    matrix2.append(row)

# Преобразуем в массивы NumPy
matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

# Вычисляем среднеквадратичное отклонение
msd = np.mean((matrix1 - matrix2) ** 2)

# Округляем до 2 знаков после запятой
print(f"{msd:.2f}")