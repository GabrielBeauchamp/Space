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

class PlayerShip:
  
  def __init__(self, speed):
    self.xpos = 0
    self.ship = pygame.image.load('data/1.png').convert()
    self.speed = speed
    self.alive = True
    self.missile = Missile('p', 5)
    self.isMoving = False
    self.movDir = ''

  def Move(self, dir):
    if dir == 'r':
      if self.xpos < WIN_HAUTEUR - SPRITE_SIZE: 
        self.xpos += self.speed
    if dir == 'l':
      if self.xpos > 0:
        self.xpos -= self.speed

  def Fire(self):
    self.missile = Missile('p', 5)
    self.missile.SetXpos(self.xpos)

    self.missile.Fire()

  def Die(self):
    pass
