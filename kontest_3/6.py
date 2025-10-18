import numpy as np

# Читаем размеры матрицы
k, m = map(int, input().split())

# Читаем матрицу
matrix = []
for _ in range(k):
    row = list(map(int, input().split()))
    matrix.append(row)

# Преобразуем в массив NumPy
matrix = np.array(matrix)

# Вычисляем n_t - количество документов, в которых встречается каждое слово
# Если элемент > 0, значит слово встречается в документе
n_t = np.sum(matrix > 0, axis=0)

# Вычисляем IDF по формуле
N = k  # количество документов
idf = np.log(N / (n_t + 1)) + 1

# Округляем до 2 знаков после запятой
idf_rounded = np.round(idf, 2)

# Выводим результат
print(' '.join(map(str, idf_rounded)))