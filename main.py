import pygame
from coins import *
from enemies import *
from settings import *
from player import *
from blocks import *

#Schtuffff
score = 0
riches = pygame.sprite.Group()
army = pygame.sprite.Group()

#Other Schtuffff
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

def game():
    #sprites
    player = Player((0, 0))
    block = Block()
    enemy = Enemy()

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

        # extra_mechanics
        if pygame.sprite.collide_mask(player, enemy):
            game_over = True
        if pygame.sprite.collide_mask(player, coin):
            score += 100
            riches.remove(coin)

        #rendering
        screen.fill((0, 0, 0))
        player.draw(screen)
        block.draw(screen)

        #update
        player.update("1")
        pygame.display.update()

game()