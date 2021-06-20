import pygame
from settings import *

class Block(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((400, 30))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        self.rect.y = 600
        self.rect.x = 100

    def draw(self, screen):
        screen.blit(self.image, self.rect)