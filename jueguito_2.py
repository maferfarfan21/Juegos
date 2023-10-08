import pygame
import sys
from pygame.locals import *

pygame.init()

ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Piedra,papel o tijera")
game = True

#Piedra papel tijeras
colorFondo = (232, 254, 255)
imagen = pygame.image.load("imagenes/piedra_papel_tijeras_.png")
pos1X, pos1Y = (5,10)

#Start
imagen_start=pygame.image.load("imagenes/start.png")
imagen_start_small= pygame.transform.scale(imagen_start,(150,90))
pos2X, pos2Y = (250,350)

#autoras
pos3X, pos3Y = (280,450)
colorTextoAutoras = (242,165,204)
fuente_autoras = pygame.font.SysFont("Times", 15)
autoras = fuente_autoras.render("Carla y Mafer", True, (colorTextoAutoras)) 
#textos
texto= pygame.font.SysFont("Arial", 30)
texto2= pygame.font.SysFont("consolas", 30)
negro= (0, 0, 0)

#boton
#boton = pygame.Rect(imagen_start_small)



while game:
    ventana.fill(colorFondo)
    ventana.blit(imagen,(pos1X,pos1Y))
    ventana.blit(imagen_start_small,(pos2X, pos2Y))
    ventana.blit(autoras,(pos3X, pos3Y))
    #tiempo que lleva abierto el programa 
    tiempo = pygame.time.get_ticks() / 1000 
    tiempo_transcurrido= texto.render( str(tiempo),True, negro)
    #puntos conseguidos
    #texto_puntos = texto2.render("Puntos: "+str(Variable de puntos),True,negro)
    #ventana.blit(texto_puntos(640, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        
    pygame.display.flip()

