import matplotlib.pyplot as plt
import random


def f(x):
    return x * x


def midpoint_displacement(xL, yL, xR, yR, roughness, threshold):
    if abs(xR - xL) < threshold:
        return [(xL, yL), (xR, yR)]

    xM = (xL + xR) / 2
    yM = (yL + yR) / 2 + (random.random() * 2 - 1) * roughness * abs(xR - xL)

    roughness/=2
    left_segment = midpoint_displacement(xL, yL, xM, yM, roughness, threshold)
    right_segment = midpoint_displacement(xM, yM, xR, yR, roughness, threshold)

    return left_segment + right_segment[1:]


def generate_terrain(width, height, roughness, threshold):
    global terrain

    terrain = midpoint_displacement(0, height // 2, width, height // 2, roughness, threshold)

    return terrain


def plot_terrain(terrain):
    x = [point[0] for point in terrain]
    y = [point[1]  for point in terrain]
    # print(x)
    # print(max(y))
    plt.fill_between(x, y, min(y) - 10, color='black')
    plt.fill_between(x, y, max(y) + 10, color='blue')
    plt.plot(x, y, color='green')

    plt.axis('off')
    plt.show()


# Настройки
width = 500  # Ширина изображения
height = 500  # Высота изображения
threshold = 1  # Пороговое значение длины отрезка
C = 0.5


R = 400
terrain = generate_terrain(width, height, R, threshold)
plot_terrain(terrain)