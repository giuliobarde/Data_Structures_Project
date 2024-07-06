import pygame
import pygame.font

pygame.init()

WIDTH = 900
HEIGHT = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

SQUARE_SIZE = 50
PADDING = 10
FONT_SIZE = 32
FPS = 60
FONT = pygame.font.Font(None, FONT_SIZE)

def draw_display(WINDOW, color):
    WINDOW.fill(color)
    pygame.display.flip()

def display_array(WINDOW, array, highlight_indices=None):
    if highlight_indices is None:
        highlight_indices = []
    
    for index, number in enumerate(array):
        x = PADDING + index * (SQUARE_SIZE + PADDING)
        y = (HEIGHT - SQUARE_SIZE) // 4

        pygame.draw.rect(WINDOW, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
        
        outline_color = (255, 0, 0) if index in highlight_indices else (0, 0, 0)
        pygame.draw.rect(WINDOW, outline_color, (x, y, SQUARE_SIZE, SQUARE_SIZE), 1)

        text_surface = FONT.render(str(number), True, BLACK)
        text_rect = text_surface.get_rect(center=(x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2))
        WINDOW.blit(text_surface, text_rect)

    pygame.display.flip()

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLACK
        self.text = text
        self.text_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = GREY if self.active else BLACK
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isnumeric():
                        self.text += event.unicode
                self.text_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.text_surface.get_width()+10)
        self.rect.w = width

    def draw(self, WINDOW):
        WINDOW.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(WINDOW, self.color, self.rect, 2)


class RadioButton:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.color = BLACK
        self.selected = False
        self.text = text
        self.text_surface = FONT.render(text, True, self.color)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.selected = not self.selected

    def draw(self, WINDOW):
        pygame.draw.circle(WINDOW, BLACK, self.rect.center, 10, 2)
        if self.selected:
            pygame.draw.circle(WINDOW, BLACK, self.rect.center, 5)
        WINDOW.blit(self.text_surface, (self.rect.x + 30, self.rect.y))

class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLACK
        self.text = text
        self.text_surface = FONT.render(text, True, WHITE)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print("Submit clicked")

    def draw(self, WINDOW):
        pygame.draw.rect(WINDOW, self.color, self.rect)
        WINDOW.blit(self.text_surface, (self.rect.x + 30, self.rect.y))