import pygame
import random
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)

pygame.display.set_caption("Скворцова Арина Владимировна")
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen.fill(WHITE)

pygame.draw.circle(screen, 'red', [200, 100], 30)
pygame.draw.circle(screen, 'orange', (200, 400), 50, 15)
pygame.draw.circle(screen, 'purple', (screen.get_width() // 2, screen.get_height() // 2), 100)
pygame.draw.rect(screen, 'blue', (400, 20, 300, 200))

for _ in range(5):
    x, y = random.randint(0, 700), random.randint(0, 500)
    w, h = random.randint(30, 100), random.randint(30, 100)
    color = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    pygame.draw.rect(screen, color, (x, y, w, h))

# домик
pygame.draw.line(screen, BLACK, (300, 300), (500, 300), 3)  # основание крыши
pygame.draw.line(screen, BLACK, (300, 300), (400, 170), 3)  # левая сторона крыши
pygame.draw.line(screen, BLACK, (400, 170), (500, 300), 3)  # правая сторона крыши

pygame.draw.line(screen, BLACK, (300, 300), (300, 450), 3)  # левая стенка
pygame.draw.line(screen, BLACK, (500, 300), (500, 450), 3)  # правая стенка
pygame.draw.line(screen, BLACK, (300, 450), (500, 450), 3)  # основание дома

# дверь
pygame.draw.line(screen, BLACK, (375, 450), (375, 375), 3)  # левая сторона двери
pygame.draw.line(screen, BLACK, (425, 450), (425, 375), 3)  # правая сторона двери
pygame.draw.line(screen, BLACK, (375, 375), (425, 375), 3)  # верх двери

# окно
pygame.draw.line(screen, BLACK, (320, 320), (360, 320), 3)  # верх окна
pygame.draw.line(screen, BLACK, (320, 360), (360, 360), 3)  # низ окна
pygame.draw.line(screen, BLACK, (320, 320), (320, 360), 3)  # левая сторона окна
pygame.draw.line(screen, BLACK, (360, 320), (360, 360), 3)  # правая сторона окна
pygame.draw.line(screen, BLACK, (340, 320), (340, 360), 3)  # вертикальная линия окна
pygame.draw.line(screen, BLACK, (320, 340), (360, 340), 3)  # горизонтальная линия окна

dots = [
    (600, 200), (650, 250), (620, 300), (680, 320),
    (720, 280), (700, 230), (660, 180), (600, 200)
]
pygame.draw.lines(screen, GREEN, True, dots, 2)

# изображение
diman = pygame.image.load("/Users/angryissues/Desktop/diman.jpg")
diman = pygame.transform.scale(diman, (100, 100))

old_x, old_y = 100, 100
old_rect = pygame.Rect(old_x, old_y, 100, 100)

background = screen.subsurface(old_rect).copy()

screen.blit(diman, (old_x, old_y))
pygame.display.flip()
start_time = pygame.time.get_ticks()

move_delay = 5000

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if (pygame.time.get_ticks() - start_time >= move_delay):
        screen.blit(background, (old_x, old_y))

        new_x, new_y = 600, 100
        new_rect = pygame.Rect(new_x, new_y, 100, 100)

        background_new = screen.subsurface(new_rect).copy()

        screen.blit(diman, (new_x, new_y))
        pygame.display.flip()

pygame.quit()

