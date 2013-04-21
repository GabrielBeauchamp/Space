#!/usr/bin/env python
import sys
import random
import math
import os
import getopt
import pygame
from pygame.locals import *
from screen import *
from playerShip import *

class Missile:
    
    def __init__(self, who, speed):
        self.fired = False
        self.xpos = 0
        self.ypos = 0
        
        if who == 'p':
            self.missile = pygame.image.load('data/pMissile.jpg').convert()
            self.speed = speed
        elif who == 'a':
            #Prend le missile alien
            #self.missile = pygame.image.load
            #self.speed = speed
            pass

    def Fire(self):
        self.fired = True
        self.xpos += self.speed
        self.ypos += self.speed
        
    def SetXpos(self, x):
        self.xpos = x

    def SetYpos(self, y):
        self.ypos = y
