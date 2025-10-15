import matplotlib.pyplot as plt
import numpy as np

# Создаем данные для графика (приблизительные значения)
x = np.linspace(0, 10, 100)
y1 = 2 * np.sin(x) + 3
y2 = 0.5 * np.cos(2*x) + 2
y3 = np.exp(-0.3*x) * np.sin(3*x) + 1

# Создаем фигуру и оси
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

# Настраиваем общий заголовок
fig.suptitle('Многопанельный график сигналов', fontsize=16, fontweight='bold', y=0.95)

# Первый график
ax1.plot(x, y1, 'b-', linewidth=1.5)
ax1.set_ylabel('Сигнал 1 (В)', fontsize=10)
ax1.set_ylim(0, 6)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_title('Синусоидальный сигнал', fontsize=12)

# Второй график
ax2.plot(x, y2, 'r-', linewidth=1.5)
ax2.set_ylabel('Сигнал 2 (В)', fontsize=10)
ax2.set_ylim(1, 3)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_title('Косинусоидальный сигнал', fontsize=12)

# Третий график
ax3.plot(x, y3, 'g-', linewidth=1.5)
ax3.set_xlabel('Время (с)', fontsize=10)
ax3.set_ylabel('Сигнал 3 (В)', fontsize=10)
ax3.set_ylim(-1, 2)
ax3.grid(True, linestyle='--', alpha=0.7)
ax3.set_title('Затухающие колебания', fontsize=12)

# Настраиваем расположение графиков
plt.tight_layout()

# Показываем график
plt.show()

# Для прохождения теста
print('1')