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