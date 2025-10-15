import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

# Загружаем изображение из локального файла
try:
    img = Image.open("Lenna.png")
except:
    # Если файл не найден, создаем случайное изображение для демонстрации
    img_array = np.random.rand(128, 128, 3)
else:
    # Уменьшаем размер изображения до 128x128 пикселей
    img_resized = img.resize((128, 128), Image.Resampling.LANCZOS)
    img_array = np.array(img_resized)

# Создаем график
plt.figure(figsize=(8, 8))
plt.imshow(img_array)
plt.axis('off')  # Отключаем оси
plt.title('Изображение Лены (128x128)', fontsize=14, pad=20)
plt.tight_layout()
plt.show()

print('1')