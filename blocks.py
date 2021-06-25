import pygame
import pyganim
from pygame import *
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ANIMATION_BLOCKTELEPORT = [
            ('assets/images/portal/portal1.png'),
            ('assets/images/portal/portal2.png'),
            ('assets/images/portal/portal3.png'),
            ('assets/images/portal/portal4.png'),
            ('assets/images/portal/portal5.png'),
            ('assets/images/portal/portal6.png'),
            ('assets/images/portal/portal7.png'),
            ('assets/images/portal/portal8.png')]
class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("assets/images/blocks/platform.png")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
class BlockDie1(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("assets/images/blocks/dieBlock1.png")
class BlockDie2(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("assets/images/blocks/dieBlock2.png")
class GhostBlock(Platform):
    def __init__(self, x, y, images):
        Platform.__init__(self, x, y)
        if images == '':
            self.image = image.load("assets/images/blocks/platform.png")
        else:
            self.image = images
class BlockTeleport(Platform):
    def __init__(self, x, y, goX, goY):
        Platform.__init__(self, x, y)
        self.goX = goX
        self.goY = goY
        self.image = pygame.image.load('assets/images/portal/portal1.png')
        boltAnim = []
        for anim in ANIMATION_BLOCKTELEPORT:
            boltAnim.append((anim, 0.1))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()
    def update(self):
        self.image.set_colorkey((41, 56, 86))
        self.boltAnim.blit(self.image, self.image.get_rect())

class Exit(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("assets/images/door/door1.png")
    def update(self):
        self.blit(self.image, (0, 0))