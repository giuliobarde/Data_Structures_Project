import pygame

pygame.init()

WIDTH = 900
HEIGHT = 500
WHITE = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
SQUARE_SIZE = 50
PADDING = 10
FONT_SIZE = 24
FPS = 60
font = pygame.font.Font(None, FONT_SIZE)

def draw_display(WINDOW, color):
    WINDOW.fill(color)

def display_array(WINDOW, array, highlight_indices=None):
    if highlight_indices is None:
        highlight_indices = []
    
    for index, number in enumerate(array):
        x = PADDING + index * (SQUARE_SIZE + PADDING)
        y = (HEIGHT - SQUARE_SIZE) // 4

        pygame.draw.rect(WINDOW, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
        
        outline_color = (255, 0, 0) if index in highlight_indices else (0, 0, 0)
        pygame.draw.rect(WINDOW, outline_color, (x, y, SQUARE_SIZE, SQUARE_SIZE), 1)

        text_surface = font.render(str(number), True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2))
        WINDOW.blit(text_surface, text_rect)

    pygame.display.flip()