#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import sys

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
level__number_open = open(r"save.txt", "r+")
level__number = int(level__number_open.read(1))
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
    levelmenubutton = Button(r"assets/design/levelmenubutton.png", (735, 443))
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
                if levelmenubutton.rect.collidepoint(pygame.mouse.get_pos()):
                    levelmenu()
                if exitbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        # rendering
        screen.blit(pygame.image.load('assets/images/bg/bgm.jpg'), (0,0))
        screen.blit(game_caption, (700, 95))
        playbutton.draw(screen)
        levelmenubutton.draw(screen)
        exitbutton.draw(screen)
        # updates
        pygame.display.update()

def levelmenu():
    global level__number

    clock = pygame.time.Clock()
    backbtn = Button(r"assets/images/btns/backbtn.png", (76, 92))
    level1btn = Button(r"assets/images/btns/notbtn.png", (333, 92))
    level2btn = Button(r"assets/images/btns/notbtn2.png", (333, 159))
    level3btn = Button(r"assets/images/btns/notbtn3.png", (333, 225))
    level4btn = Button(r"assets/images/btns/notbtn4.png", (333, 292))
    level5btn = Button(r"assets/images/btns/notbtn5.png", (333, 360))

    running = True
    while running:

        clock.tick(60)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if backbtn.rect.collidepoint(pygame.mouse.get_pos()):
                    mainmenu()
                if level1btn.rect.collidepoint(pygame.mouse.get_pos()):
                    level__number = 1
                    level_load = open(r"save.txt", "r+")
                    level_load.write("1")
                    level_load.close()
                    main()
                if level2btn.rect.collidepoint(pygame.mouse.get_pos()):
                    level__number = 2
                    level_load = open(r"save.txt", "r+")
                    level_load.write("2")
                    level_load.close()
                    main()
                if level3btn.rect.collidepoint(pygame.mouse.get_pos()):
                    level__number = 3
                    level_load = open(r"save.txt", "r+")
                    level_load.write("3")
                    level_load.close()
                    main()
                if level4btn.rect.collidepoint(pygame.mouse.get_pos()):
                    level__number = 4
                    level_load = open(r"save.txt", "r+")
                    level_load.write("4")
                    level_load.close()
                    main()
                if level5btn.rect.collidepoint(pygame.mouse.get_pos()):
                    level__number = 5
                    level_load = open(r"save.txt", "r+")
                    level_load.write("5")
                    level_load.close()
                    main()

        screen.blit(pygame.image.load('assets/images/bg/bgg.png'), (0, 0))
        backbtn.draw(screen)
        level1btn.draw(screen)
        level2btn.draw(screen)
        level3btn.draw(screen)
        level4btn.draw(screen)
        level5btn.draw(screen)
        pygame.display.update()


def main():
    global screen, entities, animatedEntities, platforms, level__number
    entities = pygame.sprite.Group()
    animatedEntities = pygame.sprite.Group()
    loadLevel()
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Fall Of Darkness")
    bg = pygame.image.load(r'assets/images/bg/bgg.png')

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
            if col == "_":
                pf = Platform1(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "-":
                pf = Platform2(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "^":
                bd = BlockDie1(x, y)
                entities.add(bd)
                platforms.append(bd)
            if col == "*":
                bd = BlockDie2(x, y)
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
                sys.exit()
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
    else:
        level__number+=1
        level_load = open(r"save.txt", "r+")
        level_load.write(str(level__number))
        print(level__number)
        level_load.close()
        main()

def loadLevel(level_num=""):
    global level, entities, animatedEntities, platforms
    level = []
    entities = pygame.sprite.Group()
    animatedEntities = pygame.sprite.Group()
    platforms = []
    global playerX, playerY
    level_load = open(r"save.txt", "r+")
    level_num = level_load.read(1)

    if level_num == "1":
        levelFile = open('assets/levels/lv1.txt')
    elif level_num == "2":
        levelFile = open('assets/levels/lv2.txt')
    elif level_num == "3":
        levelFile = open('assets/levels/lv3.txt')
    elif level_num == "4":
        levelFile = open('assets/levels/lv4.txt')
    elif level_num == "5":
        levelFile = open('assets/levels/lv5.txt')
    else:
        mainmenu()
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