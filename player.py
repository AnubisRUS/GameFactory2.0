#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyganim
from pygame import *
import blocks
MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35 # Сила, которая будет тянуть нас вниз
MOVE_EXTRA_SPEED = 2.5 # Ускорение
JUMP_EXTRA_POWER = 1 # дополнительная сила прыжка
ANIMATION_SUPER_SPEED_DELAY = 0.05 # скорость смены кадров при ускорении
ANIMATION_DELAY = 0.1 # скорость смены кадров
ANIMATION_RIGHT = [('assets/images/player/bzr1.png'),
            ('assets/images/player/bzr2.png'),
            ('assets/images/player/bzr3.png'),
            ('assets/images/player/bzr4.png')]
ANIMATION_LEFT = [('assets/images/player/bzl1.png'),
            ('assets/images/player/bzl2.png'),
            ('assets/images/player/bzl3.png'),
            ('assets/images/player/bzl4.png')]
ANIMATION_JUMP_LEFT = [('assets/images/player/bzl2.png', 0.1)]
ANIMATION_JUMP_RIGHT = [('assets/images/player/bzr2.png', 0.1)]
ANIMATION_JUMP = [('assets/images/player/bz0.png', 0.1)]
ANIMATION_STAY = [('assets/images/player/bz0.png', 0.1)]
class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image.set_colorkey(Color(COLOR))
        #        Анимация движения вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()
        boltAnim = []
        boltAnimSuperSpeed = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
            boltAnimSuperSpeed.append((anim, ANIMATION_SUPER_SPEED_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        self.boltAnimRightSuperSpeed = pyganim.PygAnimation(boltAnimSuperSpeed)
        self.boltAnimRightSuperSpeed.play()
        #        Анимация движения влево
        boltAnim = []
        boltAnimSuperSpeed = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
            boltAnimSuperSpeed.append((anim, ANIMATION_SUPER_SPEED_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        self.boltAnimLeftSuperSpeed = pyganim.PygAnimation(boltAnimSuperSpeed)
        self.boltAnimLeftSuperSpeed.play()
    def update(self, left, right, up, running, platforms):
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
                if running and (left or right):  # если есть ускорение и мы движемся
                    self.yvel -= JUMP_EXTRA_POWER  # то прыгаем выше
                self.image.fill(Color(COLOR))
                self.boltAnimJump.blit(self.image, (0, 0))

        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(Color(COLOR))
            if running:  # если ускорение
                self.xvel -= MOVE_EXTRA_SPEED  # то передвигаемся быстрее
                if not up:  # и если не прыгаем
                    self.boltAnimLeftSuperSpeed.blit(self.image, (0, 0))  # то отображаем быструю анимацию
            else:  # если не бежим
                if not up:  # и не прыгаем
                    self.boltAnimLeft.blit(self.image, (0, 0))  # отображаем анимацию движения
            if up:  # если же прыгаем
                self.boltAnimJumpLeft.blit(self.image, (0, 0))  # отображаем анимацию прыжка

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))
            if running:
                self.xvel += MOVE_EXTRA_SPEED
                if not up:
                    self.boltAnimRightSuperSpeed.blit(self.image, (0, 0))
            else:
                if not up:
                    self.boltAnimRight.blit(self.image, (0, 0))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))
        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if isinstance(p, blocks.BlockDie):  # если пересакаемый блок - blocks.BlockDie
                    self.die()  # умираем
                else:
                    if xvel > 0:  # если движется вправо
                        self.rect.right = p.rect.left  # то не движется вправо
                    if xvel < 0:  # если движется влево
                        self.rect.left = p.rect.right  # то не движется влево
                    if yvel > 0:  # если падает вниз
                        self.rect.bottom = p.rect.top  # то не падает вниз
                        self.onGround = True  # и становится на что-то твердое
                        self.yvel = 0  # и энергия падения пропадает
                    if yvel < 0:  # если движется вверх
                        self.rect.top = p.rect.bottom  # то не движется вверх
                        self.yvel = 0  # и энергия прыжка пропадает

    def die(self):
        time.wait(500)
        self.teleporting(self.startX, self.startY)  # перемещаемся в начальные координаты

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
