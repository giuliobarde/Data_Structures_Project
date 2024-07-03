import pygame
from Constants import *
from Sorting_Algorithms import *

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Data Structures Project")

def main():
    clock = pygame.time.Clock()
    run = True
    array = [99, 4, 2, 5, 7, 3, 8, 33, 1]
    sorting_steps = insertionSort(array)
    current_array = array[:]
    highlight_indices = []

    step_timer = pygame.time.get_ticks()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_display(WINDOW, WHITE)
        display_array(WINDOW, current_array, highlight_indices)

        if pygame.time.get_ticks() - step_timer > 500:
            try:
                current_array, i, j = next(sorting_steps)
                highlight_indices = [i, j]
                step_timer = pygame.time.get_ticks()
            except StopIteration:
                highlight_indices = []

    pygame.quit()

if __name__ == "__main__":
    main()