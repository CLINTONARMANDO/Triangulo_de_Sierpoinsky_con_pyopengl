from json.tool import main
import pygame
from pygame.locals import *

from OpenGL.GL import *

from math import *

def sierpi(cor1x,cor1y,cor2x,cor2y,cor3x,cor3y,n):
    
    ax=(cor1x+cor2x)/2
    ay=(cor1y+cor2y)/2
    bx=(cor1x+cor3x)/2
    by=(cor1y+cor3y)/2
    cx=(cor2x+cor3x)/2
    cy=(cor2y+cor3y)/2
    if (n==0):
        return n
    else :
        triangle (cor1x,cor1y,cor2x,cor2y,cor3x,cor3y)
        sierpi(ax,ay,bx,by,cor1x,cor1y,n-1)
        sierpi(cor3x,cor3y,bx,by,cx,cy,n-1)
        sierpi(ax,ay,cor2x,cor2y,cx,cy,n-1)


def triangle (cor1x,cor1y,cor2x,cor2y,cor3x,cor3y):
    glBegin(GL_LINE_LOOP)
    glColor3fv([1,0,0])
    glVertex2f(cor1x,cor1y)
    glVertex2f(cor2x,cor2y)
    glVertex2f(cor3x,cor3y)
    glEnd()




def Main():
    # Aqui va todo el codigo necesario
    pantalla = [800, 800]
    Cerrar = False

    pygame.init()
    pygame.display.set_mode(pantalla, DOUBLEBUF|OPENGL)

    while not Cerrar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Cerrar = True

        # Limpiar la pantalla antes de renderizar los grÃ¡ficos
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # Pintamos las primitivas
        sierpi(-0.5,-0.5,0.5,-0.5,0,0.5,10)
        pygame.display.flip()
        pygame.time.wait(60)
        
    pygame.quit()

Main()