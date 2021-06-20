import pygame
from settings import *

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, coordinate):
        super().__init__()

        self.startXY = coordinate
        self.image = pygame.image.load(r"ball.png")
        self.rect = self.image.get_rect()
        self.onGround = False

        self.rect.x = 150

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, platforms):
        if not self.onGround:
            self.rect.y += GRAVITY

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= 5
        elif key[pygame.K_d]:
            self.rect.x += 5