import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60  # кадров в секунду

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимация фигур в Pygame")
clock = pygame.time.Clock()

def random_color():
    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))

# СОЗДАЁМ ФИГУРЫ

figures = [
    {
        "type": "square",
        "x": 50,
        "y": 50,
        "size": 60,          # длина стороны квадрата
        "speed_x": 3,
        "color": random_color(),
    },
    {
        "type": "rect",
        "x": 200,
        "y": 100,
        "width": 100,
        "height": 50,
        "speed_x": 4,
        "color": random_color(),
    },
    {
        "type": "circle",
        "x": 400,            # для круга x, y будет центром
        "y": 200,
        "radius": 40,
        "speed_x": 2,
        "color": random_color(),
    },
    {
        "type": "triangle",
        "x": 600,
        "y": 300,
        "width": 80,         # основание треугольника
        "height": 60,        # высота треугольника
        "speed_x": 5,
        "color": random_color(),
    }
]

# Функция для получения списка вершин треугольника
# Допустим, треугольник "смотрит" вершиной вверх
def get_triangle_points(x, y, width, height):
    # x, y — верхний левый угол ограничивающего прямоугольника
    # вершины треугольника:
    p1 = (x, y + height)           # левая нижняя
    p2 = (x + width // 2, y)       # верхняя
    p3 = (x + width, y + height)   # правая нижняя
    return [p1, p2, p3]

# функция проверки, попала ли точка (mx, my) внутрь фигуры
def is_point_in_figure(mx, my, figure):
    ftype = figure["type"]
    
    if ftype == "square":
        x, y = figure["x"], figure["y"]
        size = figure["size"]
        return (x <= mx <= x + size) and (y <= my <= y + size)

    elif ftype == "rect":
        x, y = figure["x"], figure["y"]
        w, h = figure["width"], figure["height"]
        return (x <= mx <= x + w) and (y <= my <= y + h)

    elif ftype == "circle":
        cx, cy = figure["x"], figure["y"]
        r = figure["radius"]
        # расстояние от точки клика до центра круга
        return (mx - cx)**2 + (my - cy)**2 <= r**2

    elif ftype == "triangle":
        x, y = figure["x"], figure["y"]
        w, h = figure["width"], figure["height"]
        return (x <= mx <= x + w) and (y <= my <= y + h)

    return False

# ГЛАВНЫЙ ЦИКЛ ПРОГРАММЫ
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            # попали ли кликом в какую-нибудь фигуру
            for fig in figures:
                if is_point_in_figure(mx, my, fig):
                    fig["color"] = random_color()

    # проверки столкновений с границами
    for fig in figures:
        # только по оси X
        fig["x"] += fig["speed_x"]

        # границы
        if fig["type"] == "square":
            size = fig["size"]
            if fig["x"] < 0:  # слева
                fig["x"] = 0
                fig["speed_x"] = -fig["speed_x"]
            elif fig["x"] + size > WIDTH:  # справа
                fig["x"] = WIDTH - size
                fig["speed_x"] = -fig["speed_x"]

        elif fig["type"] == "rect":
            w = fig["width"]
            if fig["x"] < 0:
                fig["x"] = 0
                fig["speed_x"] = -fig["speed_x"]
            elif fig["x"] + w > WIDTH:
                fig["x"] = WIDTH - w
                fig["speed_x"] = -fig["speed_x"]

        elif fig["type"] == "circle":
            r = fig["radius"]
            if fig["x"] - r < 0:
                fig["x"] = r
                fig["speed_x"] = -fig["speed_x"]
            elif fig["x"] + r > WIDTH:
                fig["x"] = WIDTH - r
                fig["speed_x"] = -fig["speed_x"]

        elif fig["type"] == "triangle":
            w = fig["width"]
            if fig["x"] < 0:
                fig["x"] = 0
                fig["speed_x"] = -fig["speed_x"]
            elif fig["x"] + w > WIDTH:
                fig["x"] = WIDTH - w
                fig["speed_x"] = -fig["speed_x"]

    # ОТРИСОВКА
    screen.fill((255, 255, 255))

    for fig in figures:
        ftype = fig["type"]
        color = fig["color"]
        
        if ftype == "square":
            pygame.draw.rect(screen, color,
                             (fig["x"], fig["y"], fig["size"], fig["size"]))

        elif ftype == "rect":
            pygame.draw.rect(screen, color,
                             (fig["x"], fig["y"], fig["width"], fig["height"]))

        elif ftype == "circle":
            pygame.draw.circle(screen, color,
                               (fig["x"], fig["y"]), fig["radius"])

        elif ftype == "triangle":
            points = get_triangle_points(fig["x"], fig["y"],
                                         fig["width"], fig["height"])
            pygame.draw.polygon(screen, color, points)

    pygame.display.flip()

pygame.quit()