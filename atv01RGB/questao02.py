import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar imagem médica em tons de cinza
image = cv2.imread('tronco.png', 0)

# Cria imagem RGB de saída
pseudo = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

# Fatiamento de intensidade (a)
pseudo[(image >= 0) & (image <= 63)] = [0, 0, 255]       # Azul
pseudo[(image >= 64) & (image <= 127)] = [0, 255, 0]     # Verde
pseudo[(image >= 128) & (image <= 191)] = [255, 255, 0]  # Amarelo
pseudo[(image >= 192) & (image <= 255)] = [255, 0, 0]    # Vermelho

# Exibição
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1); plt.imshow(image, cmap='gray'); plt.title('Original'); plt.axis('off')
plt.subplot(1, 2, 2); plt.imshow(pseudo); plt.title('Pseudocoloração'); plt.axis('off')
plt.show()

# A) Divide intensidades 0–255 em 4 faixas e atribui Azul, Verde, Amarelo e Vermelho.

# B) Cores destacam faixas de intensidade que o olho confunde em cinza; na tronco.png,
# o vaso (vermelho) e os rins (amarelo) ficam mais fáceis de distinguir.

# C) Vantagem: melhora contraste visual e facilita análise de estruturas.
#    Limitação: cores são arbitrárias e podem induzir interpretação incorreta dos dados.
