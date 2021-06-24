#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame
from pygame import *
from player import *
from blocks import *
from buttons import *
# Объявляем переменные
WIN_WIDTH = 1200  # Ширина создаваемого окна
WIN_HEIGHT = 700  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#3b687b"
pygame.init()
screen = pygame.display.set_mode(DISPLAY)
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-WIN_HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return Rect(l, t, w, h)

def mainmenu():
    fnpx = pygame.font.Font("assets/fonts/ancient-modern-tales-font/AncientModernTales-a7Po.ttf", 72)

    # sprites
    clock = pygame.time.Clock()
    game_caption = fnpx.render("Fall of Darkness", True, (255, 255, 255))
    playbutton = Button(r"assets/design/playbutton.png", (735, 281))
    exitbutton = Button(r"assets/design/exitbutton.png", (735, 580))

    running = True
    while running:

        clock.tick(60)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    main()
                if exitbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        # rendering
        screen.fill((0, 0, 0))
        screen.blit(game_caption, (700, 95))
        playbutton.draw(screen)
        exitbutton.draw(screen)
        # updates
        pygame.display.update()


def main():
    global screen
    loadLevel()
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Fall Of Darkness")
    bg = pygame.image.load('assets/images/bg/bgg.png')

    screen.blit(bg, (0,0))
    left = right = False
    up = False
    running = False
    hero = Player(playerX, playerY)
    entities.add(hero)
    timer = pygame.time.Clock()
    x = y = 0
    for row in level:
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "*":
                bd = BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)
            if col == "+":
                gb = GhostBlock(x, y, '')
                entities.add(gb)
                platforms.append(gb)
            if col == "E":
                e = Exit(x, y)
                entities.add(e)
                platforms.append(e)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0  #
    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)
    while not hero.winner:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
            if e.type == KEYDOWN and e.key == K_a:
                left = True
            if e.type == KEYDOWN and e.key == K_d:
                right = True
            if e.type == KEYUP and e.key == K_d:
                right = False
            if e.type == KEYUP and e.key == K_a:
                left = False
            if e.type == KEYDOWN and e.key == K_SPACE:
                up = True
            if e.type == KEYUP and e.key == K_SPACE:
                up = False
            if e.type == KEYDOWN and e.key == K_LSHIFT:
                running = True
            if e.type == KEYUP and e.key == K_LSHIFT:
                running = False
        screen.blit(bg, (0, 0))
        animatedEntities.update()
        camera.update(hero)
        hero.update(left, right, up, running, platforms)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()

def loadLevel():
    global playerX, playerY

    levelFile = open('assets/levels/lv1.txt')
    line = " "
    while line[0] != "/":
        line = levelFile.readline()
        if line[0] != "]":
            endLine = line.find("|")
            level.append(line[0: endLine])
        if line[0] != "":
            commands = line.split()
            if len(commands) > 1:
                if commands[0] == "player":
                    playerX = int(commands[1])
                    playerY = int(commands[2])
                if commands[0] == "portal":
                    tp = BlockTeleport(int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4]))
                    entities.add(tp)
                    platforms.append(tp)
                    animatedEntities.add(tp)
level = []
entities = pygame.sprite.Group()
animatedEntities = pygame.sprite.Group()
platforms = []
if __name__ == "__main__":
    mainmenu()

