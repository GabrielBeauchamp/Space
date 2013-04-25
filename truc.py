#!/usr/bin/env python2
import sys
import random
import math
import os
import getopt
import pygame
from pygame.locals import *

from playerShip import *
from aliens import *
from screen import *

pygame.init()
screen = pygame.display.set_mode((WIN_HAUTEUR, WIN_LARGEUR)) 

pygame.display.set_caption('Space nain d\'vader') 

player = PlayerShip(5)        # Cree un joueur, avec une vitesse de 5.

alienStack = [Aliens(0, 0), Aliens(SPRITE_SIZE, 0), Aliens(SPRITE_SIZE * 2, 0), Aliens(SPRITE_SIZE * 3, 0),
              Aliens(0, SPRITE_SIZE), Aliens(SPRITE_SIZE, SPRITE_SIZE), Aliens(SPRITE_SIZE *2, SPRITE_SIZE), Aliens(SPRITE_SIZE * 3, SPRITE_SIZE)] # Test
score = 0

def colision():

    for i in alienStack:
        if player.missile.GetRect().colliderect(i.GetRect()):
            i.Die()
            player.missile.fired = False
            
        
def uptade():
    # On deplace le joueur
    if player.isMoving:
        player.Move(player.movDir)

    # On deplace les aliens
    for i in alienStack:
        i.Move()

    # On deplace les missilles
    if player.missile.fired:
        player.missile.Move('p')
        screen.blit(player.missile.missile, (player.missile.xpos, player.missile.ypos))
        
    # On test les colisions.
    colision()
    
    # On affiche les nouvelles valeur du joueur et des aliens.
    if player.alive:
        screen.blit(player.ship, (player.xpos, WIN_LARGEUR - SPRITE_SIZE))
    elif not player.alive:
        player.Die()
    
    for i in alienStack:
        if i.alive:
            screen.blit(i.ship, (i.xpos, i.ypos))
       
   
    pygame.display.flip()


def main():
  while 1:                      # Boucle infinie d'evenement.
    screen.fill((0, 0, 0))

    for event in pygame.event.get(): # Prend l'input
      if event.type == QUIT:         # Si on quitte.
        return
      if event.type == KEYDOWN: # Si une touche est appuye.
          if event.key == K_RIGHT: # J'aimerais bien que j'ai pas a appuye sur gauche ou
             # player.Move('r')     # droite a chaque fois que je veux me deplacer
              player.isMoving = True
              player.movDir = 'r'
          if event.key == K_LEFT:
              #player.Move('l')
              player.isMoving = True
              player.movDir = 'l'
          if event.key == K_LCTRL:
              if not player.missile.fired:
                  player.Fire()
          if event.key == K_p:    # Pause
              pass
          if event.key == K_q:    # Quit
              return
      
      if event.type == KEYUP:
          if event.key == K_RIGHT:
              player.isMoving = False
              player.movDir = ''
          if event.key == K_LEFT:
              player.isMoving = True
              player.movDir = ''

    uptade()                    # Screen uptade
    

if __name__ == '__main__': main()
