import pygame
from constants import *

pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Data Structures Project")

def bubblesort(array):

    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j]  = array[j + 1] 
                array[j + 1] = temp
                yield array[:]

def main():
    clock = pygame.time.Clock()
    run = True
    array = [4, 2, 5, 7, 3]
    sorting_steps = bubblesort(array)
    current_array = array[:]

    step_timer = pygame.time.get_ticks()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_display(WINDOW, WHITE)
        display_array(WINDOW, current_array)

        if pygame.time.get_ticks() - step_timer > 1000:
            try:
                current_array = next(sorting_steps)
                step_timer = pygame.time.get_ticks()
            except StopIteration:
                pass

    pygame.quit()

if __name__ == "__main__":
    main()