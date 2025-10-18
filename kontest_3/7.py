import numpy as np

# Читаем входные данные и преобразуем в массив NumPy
data = np.array(list(map(int, input().split())))

# Находим индексы элементов в диапазоне [-100, 100]
indices = np.where((data >= -100) & (data <= 100))[0]

# Выводим индексы через пробел
print(' '.join(map(str, indices)))