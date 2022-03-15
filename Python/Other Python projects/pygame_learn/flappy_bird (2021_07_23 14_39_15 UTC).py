import pygame
import neat
import os
import random
import time

## Set window dimensions
WIN_HEIGHT = 800
WIN_WIDTH = 600

## Load all the images
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets_flappy", "bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("assets_flappy", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("assets_flappy", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("assets_flappy", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("assets_flappy", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("assets_flappy", "bg.png")))

