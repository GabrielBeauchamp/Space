#!/usr/bin/env python
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
alien = Aliens()


def colision():

    if player.missile.GetRect().colliderect(alien.GetRect()):
        print "BADAM!"          # Il y a colision

def uptade():
    
    alien.Move()                # Un seul pour l'instant.
    
    if player.missile.fired:
        player.missile.Move('p')
        screen.blit(player.missile.missile, (player.missile.xpos, player.missile.ypos))
    
    colision()
    screen.blit(player.ship, (player.xpos, WIN_LARGEUR - 70))
    screen.blit(alien.ship, (alien.xpos, alien.ypos))
    pygame.display.flip()


def main():
  while 1:                      # Boucle infinie d'evenement.
    screen.fill((0, 0, 0))

    for event in pygame.event.get(): # Prend l'input
      if event.type == QUIT:         # Si on quitte.
        return
      if event.type == KEYDOWN: # Si une touche est appuye.
        if event.key == K_RIGHT: # J'aimerais bien que j'ai pas a appuye sur gauche ou
          player.Move('r')       # droite a chaque fois que je veux me deplacer
        if event.key == K_LEFT:
          player.Move('l')
        if event.key == K_LCTRL:
            if not player.missile.fired:
                player.Fire()
        if event.key == K_p:    # Pause
            pass
        if event.key == K_q:    # Quit
            return

    uptade()                    # Screen uptade
    

if __name__ == '__main__': main()
