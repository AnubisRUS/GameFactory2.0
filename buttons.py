import pygame, sys

class Button(pygame.sprite.Sprite):

    def __init__(self, image="", pos=(0, 0)):
        super().__init__()

        #create button
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        # position
        surface = pygame.display.get_surface()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def draw(self, surface):
        surface.blit(self.image, self.rect)