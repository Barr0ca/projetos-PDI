# Exemplo de suavização

import matplotlib.pyplot as plt
import cv2
import numpy as np

# Carregar imagem
img = cv2.imread("halfLife.png", cv2.IMREAD_GRAYSCALE)

# Criar Máscaras
kernel_3x3 = np.ones((3,3), np.float32) / 9
kernel_7x7 = np.ones((10,10), np.float32) / 100

# Aplicar filtros
imagem_suavizada_3x3 = cv2.filter2D(src = img, ddepth=-1, kernel=kernel_3x3)
imagem_suavizada_7x7 = cv2.filter2D(src = img, ddepth=-1, kernel=kernel_7x7)

plt.subplot(1, 3, 1), plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Grayscale")

plt.subplot(1, 3, 2), plt.imshow(imagem_suavizada_3x3, cmap="gray")
plt.axis("off")
plt.title("3x3")

plt.subplot(1, 3, 3), plt.imshow(imagem_suavizada_7x7, cmap="gray")
plt.axis("off")
plt.title("7x7")

# Salvar imagens suavizadas
plt.show()
