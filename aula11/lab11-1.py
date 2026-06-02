import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image = cv2.imread('casas.jpg', 0)

# Cria imagem RGB de saída
pseudo = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

# Fatiamento de intensidade
pseudo[(image >= 0) & (image <= 63)] = [0, 0, 255]       # Azul
pseudo[(image >= 64) & (image <= 127)] = [0, 255, 0]     # Verde
pseudo[(image >= 128) & (image <= 191)] = [255, 255, 0]  # Amarelo
pseudo[(image >= 192) & (image <= 255)] = [255, 0, 0]    # Vermelho



# Exibição
plt.figure(figsize=(10, 5))

plt.subplot(1,2,1); plt.imshow(image, cmap='gray'); plt.title('Imagem Original'); plt.axis('off')
plt.subplot(1,2,2); plt.imshow(pseudo); plt.title('Fatiamento de Intensidade'); plt.axis('off')

plt.show()