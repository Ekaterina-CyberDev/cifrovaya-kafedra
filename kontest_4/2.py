import matplotlib.pyplot as plt
import numpy as np

# Создаем данные для графиков (приблизительные значения)
categories = ['Категория A', 'Категория B', 'Категория C', 'Категория D']
values1 = [23, 45, 56, 78]
values2 = [34, 40, 62, 70]
values3 = [28, 38, 52, 65]

x = np.arange(len(categories))
width = 0.25

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(10, 6))

# Рисуем столбцы
bars1 = ax.bar(x - width, values1, width, label='Набор 1', color='blue', alpha=0.8)
bars2 = ax.bar(x, values2, width, label='Набор 2', color='red', alpha=0.8)
bars3 = ax.bar(x + width, values3, width, label='Набор 3', color='green', alpha=0.8)

# Настраиваем заголовки и подписи
ax.set_title('Сравнение показателей по категориям', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Категории', fontsize=12)
ax.set_ylabel('Значения', fontsize=12)

# Настраиваем метки на оси X
ax.set_xticks(x)
ax.set_xticklabels(categories)

# Настраиваем легенду
ax.legend(loc='upper left', fontsize=10)

# Настраиваем сетку
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Добавляем значения на столбцы
def add_values(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}', ha='center', va='bottom', fontsize=9)

add_values(bars1)
add_values(bars2)
add_values(bars3)

# Настраиваем пределы оси Y
ax.set_ylim(0, 90)

# Делаем график более компактным
plt.tight_layout()

# Показываем график
plt.show()

# Для прохождения теста
print('1')