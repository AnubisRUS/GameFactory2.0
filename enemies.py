import pygame
import random
class Enemy():
    def __init__(self):
        super().__init__()
        screen = pygame.display.get_surface()
        self.image = pygame.image.load(r"Game-factory-final/assets/alien2.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 100)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        self.rect.x += random.randint(-20, 20)
