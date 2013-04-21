#!/usr/bin/env python
import sys
import random
import math
import os
import getopt
import pygame
from pygame.locals import *
from screen import *

class PlayerShip:
  
  def __init__(self, speed):
    self.xpos = 0
    self.ship = pygame.image.load('data/1.png').convert()
    self.speed = speed
    
  def Move(self, dir):
      if dir == 'r':
        if self.xpos < WIN_HEIGHT - 70: 
          self.xpos += self.speed
      if dir == 'l':
        if self.xpos > 0:
          self.xpos -= self.speed

  def Fire(self):
      pass
