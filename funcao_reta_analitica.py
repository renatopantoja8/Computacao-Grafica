from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Configurações da janela
window_height = 300
window_width = 300
window_title = b"Renderizar ponto com OpenGL"

def init():
    """Inicializa o ambiente OpenGL."""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Cor de fundo (preto)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, window_width, 0, window_height)  # Sistema de coordenadas 2D

def funcao_reta_analitico(x1, y1, x2, y2):
    """Desenha uma linha entre dois pontos usando a fórmula analítica."""
    glBegin(GL_POINTS)
    if x1 == x2:  # Reta vertical
        while y1 <= y2:
            glVertex2f(x1, y1)
            y1 += 1
    else:
        m = (y2 - y1) / (x2 - x1)  # Coeficiente angular
        b = y1 - m * x1  # Intercepto
        x = x1
        while x <= x2:
            y = m * x + b
            glVertex2f(x, y)
            x += 1
    glEnd()

def render():
    """Função de renderização."""
    glClear(GL_COLOR_BUFFER_BIT)  # Limpa a tela
    glColor3f(1.0, 1.0, 1.0)  # Define a cor do ponto (branco)

    # Chame aqui a função de desenhar a reta com os valores desejados
    funcao_reta_analitico(50, 50, 200, 200)

    glFlush()  # Garante a execução imediata dos comandos

def main():
    """Função principal."""
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(window_title)
    init()
    glutDisplayFunc(render)
    glutMainLoop()

if __name__ == "__main__":
    main()
