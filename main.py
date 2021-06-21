import pygame, sys
from settings import *
from main_camera import *

from player import Player
from blocks import Block

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

def game():
    #sprites
    player = Player((0, 0))
    block = Block((255, 255, 255), (0, 500))
    block1 = Block((100, 200, 100), (900, 350))

    running = True
    while running:
        clock.tick(FPS)

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        if pygame.sprite.collide_mask(player, block):
            player.onGround = True
        elif pygame.sprite.collide_mask(player, block1):
            player.onGround = True
        else:
            player.onGround = False

        #rendering
        screen.fill((0, 0, 0))
        player.draw(screen)
        block.draw(screen)
        block1.draw(screen)

        #update
        player.update("1")
        if player.rect.x > 400:
            maincamera([block, block1], player)
        pygame.display.update()

game()