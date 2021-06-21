import pygame
from settings import *

def maincamera(object_list, player):
    key = pygame.key.get_pressed()
    for object in object_list:
        if key[pygame.K_d]:
            object.rect.x -= camera_speed
        if key[pygame.K_a]:
            object.rect.x += camera_speed