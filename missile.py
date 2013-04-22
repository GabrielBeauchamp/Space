#!/usr/bin/env python2
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
        #self.ypos = 0
        
        if who == 'p':
            self.missile = pygame.image.load('data/pMissile.jpg').convert()
            self.speed = speed
            self.ypos = 530
        elif who == 'a':
            #Prend le missile alien
            #self.missile = pygame.image.load
            #self.speed = speed
            pass

    def Fire(self):
        self.setFired(True)
        
        
    def Move(self, who):
        if who == 'p':          # Player
            self.SetYpos(self.ypos - self.speed)
            if self.ypos == 0:
                self.fired = False
        elif who == 'a':        # Alien
            self.SetYpos(self.ypos + self.speed)
            
    def GetRect(self):
        return pygame.Rect(self.xpos, self.ypos, 64, 64)

    def SetXpos(self, x):
        self.xpos = x

    def SetYpos(self, y):
        self.ypos = y
    
    def setFired(self, fired):
        self.fired = fired
