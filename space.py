#!/usr/bin/env python2
import sys
import random
import math
import os
import getopt
import pygame
import random
from pygame.locals import *

from playerShip import *
from aliens import *
from screen import *

pygame.init()
screen = pygame.display.set_mode((WIN_HAUTEUR, WIN_LARGEUR)) 

pygame.display.set_caption('Space nain d\'vader') 

player = PlayerShip(5)        # Cree un joueur, avec une vitesse.


xOffset = 0
yOffset = 0
alienStack = []
deadStack = []

for i in range(2):
    yOffset = i
    for j in range(4):
        xOffset = j
        alienStack += [Aliens(SPRITE_SIZE * xOffset, SPRITE_SIZE * yOffset)]
        
def colision():
    for i in alienStack:
        if i.alive:
            if player.missile.GetRect().colliderect(i.GetRect()):
                i.Die()
                player.missile.fired = False
                
                
def deadAlien():
    for i in alienStack:
        if not i.alive:
            deadStack += i
            alienStack -= i

def update():
    # On deplace le joueur
    if player.isMoving:
        player.Move(player.movDir)

    # On deplace les aliens
    for i in alienStack:
        if i.alive:
            i.Move()
        
    # On deplace les missilles
    if player.missile.fired:
        player.missile.Move('p')
        screen.blit(player.missile.missile, (player.missile.xpos, player.missile.ypos))
        
    # On test les colisions.
    colision()
    
    # Ceci ne fonctionne pas.
    #deadAlien()
    #deadStack = []
    
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
    pause = False

    while 1:                      # Boucle infinie d'evenement.
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get(): # Prend l'input
            if event.type == QUIT:         # Si on quitte.
                return
            if event.type == KEYDOWN: # Si une touche est appuye.
                if event.key == K_RIGHT:
                    player.isMoving = True
                    player.movDir = 'r'
                if event.key == K_LEFT:
                    player.isMoving = True
                    player.movDir = 'l'
                if event.key == K_LCTRL:
                    if not player.missile.fired:
                        player.Fire()
                if event.key == K_p:    # Pause
                    if pause == False:
                        pause = True      
                    elif pause == True:
                        pause = False
                if event.key == K_q:    # Quit
                    return
      
            if event.type == KEYUP: # Si la touche n'est plus appuye.
                if event.key == K_RIGHT:
                    player.isMoving = False
                    player.movDir = ''
                if event.key == K_LEFT:
                    player.isMoving = True
                    player.movDir = ''

      #if True:                  # Ne fonctionne pas vraiment.
       #   alienStack[0].Fire()

        if pause == False:
            update()            # Screen update, si le jeu est pas en pause, bien sur.
    

if __name__ == '__main__': main()
