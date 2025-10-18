import numpy as np

# Читаем входные данные и преобразуем в массив NumPy
data = np.array(list(map(float, input().split())))

# Выполняем преобразования: квадрат → синус → минимум
result = np.sin(data ** 2)

# Находим минимальный элемент и округляем
min_value = np.min(result)
print(f"{min_value:.2f}")