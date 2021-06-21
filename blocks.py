import pygame
from settings import *

class Block(pygame.sprite.Sprite):

    def __init__(self, color, coordinates):
        super().__init__()

        self.image = pygame.Surface((800, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.y = coordinates[1]
        self.rect.x = coordinates[0]

    def draw(self, screen):
        screen.blit(self.image, self.rect)