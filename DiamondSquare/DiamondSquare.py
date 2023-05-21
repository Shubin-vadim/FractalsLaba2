import numpy as np
import matplotlib.pyplot as plt


def diamond_square(n, R, initial_heights) -> None:
    size = 2**n + 1
    height_map = np.zeros((size, size))

    # Установка начальных высот для углов квадрата
    height_map[0, 0] = initial_heights[0]
    height_map[0, size - 1] = initial_heights[1]
    height_map[size-1, 0] = initial_heights[2]
    height_map[size-1, size-1] = initial_heights[3]

    step = size - 1
    while step > 1:
        half_step = step // 2

        # Square step
        for i in range(half_step, size-1, step):
            for j in range(half_step, size-1, step):
                # Среднее арифметическое вершин сдвинутое на случайную величину
                height_map[i, j] = (height_map[i-half_step, j-half_step] +
                                    height_map[i-half_step, j+half_step] +
                                    height_map[i+half_step, j-half_step] +
                                    height_map[i+half_step, j+half_step]) / 4 + np.random.uniform(-R * half_step, R * half_step)

        # Diamond step
        for i in range(0, size-1, half_step):
            for j in range((i + half_step) % step, size-1, step):
                # Среднее арифметическое вершин сдвинутое на случайную величину
                height_map[i, j] = (height_map[(i-half_step) % size, j] +
                                    height_map[(i+half_step) % size, j] +
                                    height_map[i, (j-half_step) % size] +
                                    height_map[i, (j+half_step) % size]) / 4 + np.random.uniform(-R * half_step, R * half_step)

        step = half_step

    return height_map


# Параметры алгоритма
n = int(input("Введите размерность n: "))  # Размерность карты высот, 2^n + 1
R = float(input("Введите значение параметра R: "))  # Шероховатость

# Ввод высот углов
print("Введите высоты углов:")
top_left = float(input("Верхний левый угол: "))
top_right = float(input("Верхний правый угол: "))
bottom_left = float(input("Нижний левый угол: "))
bottom_right = float(input("Нижний правый угол: "))
initial_heights = [top_left, top_right, bottom_left, bottom_right]

# Генерация карты высот
height_map = diamond_square(n, R,  initial_heights)


# Отображение карты высот
plt.imshow(height_map, cmap='Dark2')
plt.colorbar()
plt.show()
