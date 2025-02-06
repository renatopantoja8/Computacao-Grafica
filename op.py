import cv2
import numpy as np

img = cv2.imread('Captura de Tela (15).png')

altura, largura, _ = img.shape

pontos = np.array([[100, 50], [200, 50], [250, 150], [150, 200], [50, 150]], np.int32) 
                   
cv2.polylines(img, [pontos], isClosed=True, color=(255, 0, 0), thickness=2)

centro = (largura // 2, altura // 2)
cv2.circle(img, centro, 100, (150, 255, 220), thickness=3)

cv2.imshow('Imagem com poligono', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
