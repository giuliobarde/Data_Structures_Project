import pygame
from Constants import *
from Sorting_Algorithms import *

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Data Structures Project")

array_size_input = pygame.Rect(200, 200, 240, 32)

def main():
    clock = pygame.time.Clock()
    run = True
    array = [99, 4, 2, 5, 7, 3, 8, 33, 1]
    sorting_steps = insertionSort(array)
    current_array = array[:]
    highlight_indices = []

    step_timer = pygame.time.get_ticks()

    input_box = InputBox(200, 100, 240, 32)
    radio_button = RadioButton(200, 200, "Option 1")
    button = Button(200, 300, 100, 50, "Submit")

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            input_box.handle_event(event)
            radio_button.handle_event(event)
            button.handle_event(event)

        input_box.update()

        draw_display(WINDOW, WHITE)
        input_box.draw(WINDOW)
        radio_button.draw(WINDOW)
        button.draw(WINDOW)
        #display_array(WINDOW, current_array, highlight_indices)

        pygame.display.flip()

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