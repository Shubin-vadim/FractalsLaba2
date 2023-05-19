import matplotlib.pyplot as plt
import random


def midpoint_displacement(xL, yL, xR, yR, roughness, threshold):
    if abs(xR - xL) < threshold:
        return [(xL, yL), (xR, yR)]

    xM = (xL + xR) / 2
    yM = (yL + yR) / 2 + (random.random() * 2 - 1) * roughness * abs(xR - xL)

    left_segment = midpoint_displacement(xL, yL, xM, yM, roughness, threshold)
    right_segment = midpoint_displacement(xM, yM, xR, yR, roughness, threshold)

    return left_segment + right_segment[1:]


def generate_terrain(width, height, roughness, threshold):
    global terrain
    terrain = [(0, height // 2), (width, height // 2)]

    terrain = midpoint_displacement(0, height // 2, width, height // 2, roughness, threshold)

    return terrain


def plot_terrain(terrain):
    x = [point[0] for point in terrain]
    y = [point[1] for point in terrain]

    plt.fill_between(x, y, min(y), color='black')
    plt.fill_between(x, y, max(y), color='blue')
    plt.plot(x, y, color='green')

    plt.axis('off')
    plt.show()


def update_terrain():
    terrain = generate_terrain(width, height, roughness, threshold)
    plot_terrain(terrain)


# Настройки
width = 800  # Ширина изображения
height = 400  # Высота изображения
threshold = 3 # Пороговое значение длины отрезка
scroll_offset = 200  # Смещение для скроллинга

#xl, yl, xr, yr = map(float, input().split())
roughness = 5 #float(input())
terrain = generate_terrain(width, height, roughness, threshold)
plot_terrain(terrain)