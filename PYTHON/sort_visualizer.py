import pygame
import random
import time

# Настройки окна
WIDTH, HEIGHT = 800, 600
ARRAY_SIZE = 50
BAR_WIDTH = WIDTH // ARRAY_SIZE

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)
RED = (255, 100, 100)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Алгоритмы сортировки")
font = pygame.font.Font(None, 36)

# Генерация случайного массива
def generate_array():
    return [random.randint(10, HEIGHT - 100) for _ in range(ARRAY_SIZE)]

array = generate_array()

# кнопки 
button_random = pygame.Rect(0, 550, 300, 30)
button_algorithm = pygame.Rect(320, 550, 200, 30)
button_sort = pygame.Rect(550, 550, 250, 30)

selected_algorithm = "Пузырьком"
algorithms = ["Пузырько", "Гномья" ,"Быстрая", "Поразрядная"]
algorithm_index = 0

# Функция сортировки пузырьком с визуализацией
def bubble_sort_visual():
    global array
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                screen.fill(WHITE)
                for k, value in enumerate(array):
                    color = RED if k == j or k == j + 1 else BLUE
                    pygame.draw.rect(screen, color, (k * BAR_WIDTH, HEIGHT - value - 50, BAR_WIDTH - 2, value))
                pygame.draw.rect(screen, RED, button_random)
                pygame.draw.rect(screen, RED, button_algorithm)
                pygame.draw.rect(screen, RED, button_sort)
                screen.blit(font.render("Генерировать массив", True, WHITE), (button_random.x + 30, button_random.y + 5))
                screen.blit(font.render("Отсортировать", True, WHITE), (button_sort.x + 30, button_sort.y + 5))
                screen.blit(font.render(selected_algorithm, True, WHITE), (button_algorithm.x + 30, button_algorithm.y + 5))
                pygame.display.flip()
                time.sleep(0.02)  
                
running = True
while running:
    screen.fill(WHITE)
    
    # Отрисовка массива
    for i, value in enumerate(array):
        pygame.draw.rect(screen, BLUE, (i * BAR_WIDTH, HEIGHT - value - 50, BAR_WIDTH - 2, value))
    
    # Отрисовка кнопок
    pygame.draw.rect(screen, RED, button_random)
    pygame.draw.rect(screen, RED, button_algorithm)
    pygame.draw.rect(screen, RED, button_sort)
    
    screen.blit(font.render("Генерировать массив", True, WHITE), (button_random.x + 30, button_random.y + 5))
    screen.blit(font.render("Отсортировать", True, WHITE), (button_sort.x + 30, button_sort.y + 5))
    screen.blit(font.render(selected_algorithm, True, WHITE), (button_algorithm.x + 30, button_algorithm.y + 5))
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_random.collidepoint(event.pos):
                array = generate_array()  
            elif button_algorithm.collidepoint(event.pos):
                algorithm_index = (algorithm_index + 1) % len(algorithms)
                selected_algorithm = algorithms[algorithm_index]
            elif button_sort.collidepoint(event.pos):
                bubble_sort_visual()
    
    pygame.display.flip()
    
pygame.quit()
