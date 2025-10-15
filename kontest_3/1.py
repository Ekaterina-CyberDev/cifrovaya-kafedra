import numpy as np

# Чтение входных данных и преобразование в массив NumPy
data = np.array(list(map(int, input().split())))

# Применение условия: числа > 127 заменяются на 1, остальные на 0
result = np.where(data > 127, 1, 0)

# Вывод результата
print(' '.join(map(str, result)))