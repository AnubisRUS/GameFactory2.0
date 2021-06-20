import pygame, sys
from settings import *

from player import Player
from blocks import Block

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

def game():
    #sprites
    player = Player((0, 0))
    block = Block()

    running = True
    while running:
        clock.tick(FPS)

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if pygame.sprite.collide_mask(player, block):
            player.onGround = True
        else:
            player.onGround = False

        #rendering
        screen.fill((0, 0, 0))
        player.draw(screen)
        block.draw(screen)

        #update
        player.update("1")
        pygame.display.update()

game()