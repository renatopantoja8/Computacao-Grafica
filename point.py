from OpenGL.GL import * 
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 300
window_width = 300
window_title = b"Renderizar ponto com OpenGL"


base = [
  [-0.5, -0.5],  
  [0.5, -0.5],   
  [0.5, 0.2],    
  [-0.5, 0.2]    
]

telhado = [
  [-0.6, 0.2],   
  [0, 0.7],      
  [0.6, 0.2]    
]

def init():
    glClearColor(0, 0, 0, 1)
    glPointSize(5)

def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    
    glBegin(GL_LINE_LOOP)
    glColor3f(1, 1, 1)
    for v in base:
        glVertex2fv(v)
    glEnd()
    
   
    glBegin(GL_LINE_LOOP)
    glColor3f(1, 1, 1)
    for v in telhado:
        glVertex2fv(v)
    glEnd()
    
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(window_title)
    init()
    glutDisplayFunc(render)
    glutMainLoop()

main()
