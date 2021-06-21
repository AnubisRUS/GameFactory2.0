import pygame
import random
class Coin():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"Game-factory-final/assets/Coin.png")
        screen = pygame.display.get_surface()
        self.rect = self.image.get_rect()
        #self.rect.x = random.randrange(1000, 1000)
        #self.rect.y = random.randrange(1000, 1000)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
