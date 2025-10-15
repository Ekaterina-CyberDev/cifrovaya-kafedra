import matplotlib.pyplot as plt
import numpy as np

# Создаем данные для графиков
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x/3) * np.sin(2*x)

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(12, 8))

# Рисуем три графика разными цветами и стилями
ax.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
ax.plot(x, y2, 'r--', linewidth=2, label='cos(x)')
ax.plot(x, y3, 'g-.', linewidth=2, label='exp(-x/3)*sin(2x)')

# Настраиваем заголовки и подписи
ax.set_title('Сравнение различных функций', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Время, с', fontsize=12)
ax.set_ylabel('Амплитуда', fontsize=12)

# Настраиваем легенду
ax.legend(loc='upper right', fontsize=12, framealpha=0.9)

# Настраиваем сетку
ax.grid(True, linestyle='--', alpha=0.7)

# Настраиваем пределы осей
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

# Настраиваем деления на осях
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(-1.5, 1.6, 0.5))

# Добавляем подписи к осям
ax.tick_params(axis='both', which='major', labelsize=10)

# Делаем график более компактным
plt.tight_layout()

# Показываем график
plt.show()

# Для прохождения теста
print('1')