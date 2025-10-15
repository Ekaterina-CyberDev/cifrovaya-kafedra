import numpy as np

# Читаем размеры матрицы
n, m = map(int, input().split())

# Читаем матрицу
matrix = np.array([list(map(int, input().split())) for _ in range(n)])

# Определяем ядро свертки
kernel = np.array([[-1, -1, -1],
                   [-1, 8, -1],  # Изменяем ядро на противоположное
                   [-1, -1, -1]])

# Выполняем свертку
result = np.zeros((n-2, m-2))
for i in range(3):
    for j in range(3):
        result += matrix[i:i+n-2, j:j+m-2] * kernel[i, j]

# Добавляем исходные значения (без границ)
center_values = matrix[1:n-1, 1:m-1]
result = center_values + result

# Обрезаем значения
result = np.clip(result, 0, 255).astype(int)

# Выводим результат
for row in result:
    print(' '.join(map(str, row)))