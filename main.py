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


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Data Structures Project")

font = pygame.font.Font(None, FONT_SIZE)


array = [4, 2, 5, 7, 3]

def draw_display(color):
    WINDOW.fill(color)

def display_array(array):

    for index, number in enumerate(array):

        x = PADDING + index * (SQUARE_SIZE + PADDING)
        y = (HEIGHT - SQUARE_SIZE) // 4

        pygame.draw.rect(WINDOW, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE))

        text_surface = font.render(str(number), True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2))
        WINDOW.blit(text_surface, text_rect)

    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_display(WHITE)
        display_array(array)


    pygame.quit()

if __name__ == "__main__":
    main()