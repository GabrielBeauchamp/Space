#!/usr/bin/env python2
import sys
import random
import math
import os
import getopt
import pygame
from pygame.locals import *

from screen import *
from missile import *

class Aliens:
    
    def __init__(self, x, y):
        self.ship = pygame.image.load('data/4.png').convert()
        self.speed = 0.2
        self.xpos = x
        self.ypos = y
        self.alive = True
        self.missile = Missile('a', 2)

    def Move(self):
        if self.xpos < WIN_LARGEUR - SPRITE_SIZE:
            self.xpos += self.speed
        else:
            self.xpos = 0
            self.ypos += 70

    def GetRect(self):
        return pygame.Rect(self.xpos, self.ypos, 64, 64)

    def Die(self):
        self.alive = False
        self.xpos = WIN_LARGEUR +1
        self.ypos = WIN_HAUTEUR +1

    def Fire(self):
        self.missile = Missile('a', 2)
        self.missile.SetXpos(self.xpos)
        self.missile.SetYpos(self.ypos)

        self.missile.Fire()
