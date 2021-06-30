import pygame
from pygame.locals import *
import sys
import time


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("tutorial pygame parte 2")

    fondo = pygame.image.load("avion01.jpg").convert()
    tux = pygame.image.load("tux.png").convert_alpha()
    tux02 = pygame.image.load("tux02.png").convert_alpha()
    tux03 = pygame.image.load("tux03.png").convert_alpha()
    tux04 = pygame.image.load("tux04.png").convert_alpha()

    lista=[tux, tux02, tux03, tux04]
    tamanio = len(lista)
    range(0,len(lista))

    tux_pos_x = 550
    tux_pos_y = 300

    toparriba = 0
    topderecha = 550
    topizquierda = 50
    topabajo = 300

    screen.blit(tux, (tux_pos_x, tux_pos_y))
    screen.blit(fondo, (0, 0))
    pygame.display.flip()
    
    t = True 

    while True :

        print ("x: ", tux_pos_x)
        print ("y: ", tux_pos_y)
        print("#----------------------------------------#")
        
        if tux_pos_x > 50 and t == True:
            tux_pos_x = tux_pos_x - 20
            for x in range(0,len(lista)):

                screen.blit(lista[x], (tux_pos_x, tux_pos_y))
                pygame.display.flip()
                screen.blit(fondo, (0, 0))
                pygame.time.delay(60)
                
        if tux_pos_x == 50:

            tux_pos_y = tux_pos_y - 20
            for x in range(0,len(lista)):
                
                screen.blit(lista[x], (tux_pos_x, tux_pos_y))
                pygame.display.flip()
                screen.blit(fondo, (0, 0))
                pygame.time.delay(60)
                t = False


        if tux_pos_y == toparriba and t == False:
                
                
            tux_pos_x = tux_pos_x + 20
            for x in range(0,len(lista)):

                screen.blit(lista[x], (tux_pos_x, tux_pos_y))
                pygame.display.flip()
                screen.blit(fondo, (0, 0))
                pygame.time.delay(60)

        if tux_pos_x == topderecha and t == False:
                
                
            tux_pos_y = tux_pos_y + 20
            for x in range(0,len(lista)):

                screen.blit(lista[x], (tux_pos_x, tux_pos_y))
                pygame.display.flip()
                screen.blit(fondo, (0, 0))
                pygame.time.delay(60)

        if tux_pos_y == topabajo and t == False:
                
                
            tux_pos_x = tux_pos_x - 20
            for x in range(0,len(lista)):

                screen.blit(lista[x], (tux_pos_x, tux_pos_y))
                pygame.display.flip()
                screen.blit(fondo, (0, 0))
                pygame.time.delay(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
