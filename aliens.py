#!/usr/bin/env python
import sys
import random
import math
import os
import getopt
import pygame
from pygame.locals import *
from screen import *

class Aliens:
    
    def __init__(self):
        self.ship = pygame.image.load('data/4.png').convert()
        self.speed = 0.2
        self.xpos = 0
        self.ypos = 0

    def Move(self):
        if self.xpos < WIN_LARGEUR - 70:
            self.xpos += self.speed
        else:
            self.xpos = 0
            self.ypos += 70

    def GetRect(self):
        return pygame.Rect(self.xpos, self.ypos, 64, 64)
