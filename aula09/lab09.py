# Filtros de média e mediana para suavização

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image = cv2.imread('netero.jpg', 0)

# Adicionar ruído gaussiano
mean = 0
sigma = 25
gaussian_noise = np.random.normal(mean, sigma, image.shape)

# Converter para float antes da soma
noisy_image = image.astype(np.float32) + gaussian_noise

# Imagem com ruído
plt.subplot(3, 4, 1)
plt.imshow(noisy_image, cmap='gray')
plt.title('Ruído Gaussiano')
plt.axis('off')

# Histograma da imagem ruidosa 
plt.subplot(3, 4, 2)
plt.hist(noisy_image.ravel(), 256, [0, 256], color='black')
plt.title('Histograma Ruído')

# Normalizar valores
noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

# Aplicar filtros
mean_filtered = cv2.blur(noisy_image, (5, 5))
median_filtered = cv2.medianBlur(noisy_image, 5)

# Criar figura
plt.figure(figsize=(15, 8))

# Imagem com ruído normalizado
plt.subplot(3, 4, 3)
plt.imshow(noisy_image, cmap='gray')
plt.title('Ruído Gaussiano')
plt.axis('off')

# Filtro de média
plt.subplot(3, 4, 4)
plt.imshow(mean_filtered, cmap='gray')
plt.title('Filtro de Média')
plt.axis('off')

# Filtro de mediana
plt.subplot(3, 4, 5)
plt.imshow(median_filtered, cmap='gray')
plt.title('Filtro de Mediana')
plt.axis('off')

# Histograma da imagem ruidosa normalizada
plt.subplot(3, 4, 6)
plt.hist(noisy_image.ravel(), 256, [0, 256], color='black')
plt.title('Histograma Ruído Normalizado')

# Histograma filtro média
plt.subplot(3, 4, 7)
plt.hist(mean_filtered.ravel(), 256, [0, 256], color='blue')
plt.title('Histograma Média')

# Histograma filtro mediana
plt.subplot(3, 4, 8)
plt.hist(median_filtered.ravel(), 256, [0, 256], color='red')
plt.title('Histograma Mediana')

plt.tight_layout()
plt.show()