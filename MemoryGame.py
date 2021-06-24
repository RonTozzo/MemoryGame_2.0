import pygame
import sys
import random
import string
import os.path

DIM_X = 4
DIM_Y = 3
CARD_X_SIZE = 200
CARD_Y_SIZE = 250
SCREEN_X_SIZE = CARD_X_SIZE * DIM_X
SCREEN_Y_SIZE = CARD_Y_SIZE * DIM_Y
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

colors_indices_list = [x for x in range((DIM_X * DIM_Y) // 2)] * 2
random.shuffle(colors_indices_list)

letters_list = list(string.ascii_uppercase)
random.shuffle(letters_list)

colors = []  # Lista das cores aleatórias
level_colors_ranges = [(5, 25), (7, 23), (10, 20), (12, 17), (15, 15)]
current_level = 0
cards = []  # lista das cartas
previous_card = None  # Armazenamento das cartas anteriores
opened_cards = 0
is_winner = False
is_letters = False  

# TODO: Adiciona pontuações

def fill_random_colors(n, color_range):
    lst = []
    for i in range(n):
        rand_0_255 = lambda: random.randint(color_range[0], color_range[1]) * 10
        lst.append((rand_0_255(), rand_0_255(), rand_0_255()))
    return lst


colors = fill_random_colors((DIM_X * DIM_Y) // 2, level_colors_ranges[current_level])


class BaseCard:
    def __init__(self, screen, left_top_coord, x_size, y_size):
        self.left_top_coord = left_top_coord
        self.x_size = x_size
        self.y_size = y_size
        self.screen = screen
        self.left_x_coord = self.left_top_coord[0] * self.x_size
        self.left_y_coord = self.left_top_coord[1] * self.y_size
        self.card_rect = pygame.Rect(
            (self.left_x_coord, self.left_y_coord), (self.x_size, self.y_size)
        )


class ColorCard(BaseCard):
    def __init__(self, screen, color, left_top_coord, x_size, y_size, color_index):
        super().__init__(screen, left_top_coord, x_size, y_size)
        self.color = color
        self.font = pygame.font.Font(os.path.join("fonts", "LiberationMono-Bold.ttf"), y_size)
        self.color_index = color_index
        self.hide_color_index_after_click = True

    def show_color_index(self):
        text = self.font.render(str(self.color_index), True, BLACK)
        text_rect = text.get_rect(
            center=(
                self.left_x_coord + self.x_size // 2,
                self.left_y_coord + self.y_size // 2,
            )
        )
        self.screen.blit(text, text_rect)

    def draw_card(self):
        pygame.draw.rect(self.screen, self.color, self.card_rect)
        pygame.draw.rect(self.screen, BLACK, self.card_rect, 4)

    def hide_color_index(self):
        self.draw_card()