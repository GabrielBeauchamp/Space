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
# Je dois en faire plus d'un... mais je sais pas comment.
# 
alien = Aliens(0, 0)
alienStack = [Aliens(0, 0), Aliens(70, 0)] # Test
score = 0

def colision():

    #if player.missile.GetRect().colliderect(alien.GetRect()):
    #    print "BADAM!"          # MIl y a colision
    #    alien.Die()
    #   player.missile.setFired(False)
    for i in alienStack:
        if player.missile.GetRect().colliderect(i.GetRect()):
            i.Die()
        
def uptade():
    
    #alien.Move()                
    for i in alienStack:
        i.Move()

    if player.missile.fired:
        player.missile.Move('p')
        screen.blit(player.missile.missile, (player.missile.xpos, player.missile.ypos))
    
    colision()
    if player.alive:
        screen.blit(player.ship, (player.xpos, WIN_LARGEUR - 70))
    elif not player.alive:
        player.Die()
    
    for i in alienStack:
        if i.alive:
            screen.blit(i.ship, (i.xpos, i.ypos))
    #if alien.alive:             # Si l'alien est vivant on l'affiche, sinon, bah non.
    #   screen.blit(alien.ship, (alien.xpos, alien.ypos))
    
   
    pygame.display.flip()


def main():
  while 1:                      # Boucle infinie d'evenement.
    screen.fill((0, 0, 0))

    for event in pygame.event.get(): # Prend l'input
      if event.type == QUIT:         # Si on quitte.
        return
      if event.type == KEYDOWN: # Si une touche est appuye.
          key = pygame.key.get_pressed()
          if key[pygame.K_RIGHT]: # J'aimerais bien que j'ai pas a appuye sur gauche ou
              player.Move('r')     # droite a chaque fois que je veux me deplacer
          if key[pygame.K_LEFT]:
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
