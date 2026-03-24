# Importando bibliotecas
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem:
img = cv2.imread("casas.jpg")

# Adicionar um ruído artificial:
print("Shape da imagem original:")
print(img.shape)

noise = np.random.normal(0, 25, img.shape).astype('uint8') 

print("Shape da imagem ruidosa:") # Mesmo shape
print(noise.shape)

noise_img = cv2.add(img, noise) # Somando matriz da imagem original com a imagem ruidosa

# Aplicar filtros (remover ruídos):
gaussian = cv2.GaussianBlur(noise_img, (5,5), 0)
median = cv2.medianBlur(noise_img, 5)
bilateral = cv2.bilateralFilter(noise_img, 9, 75, 75) 

# Imprimir os resultados:
plt.subplot(2, 3, 1); plt.title("Original"); plt.imshow(img)
plt.subplot(2, 3, 2); plt.title("Noise"); plt.imshow(noise_img)
plt.subplot(2, 3, 3); plt.title("Gaussian"); plt.imshow(gaussian)
plt.subplot(2, 3, 4); plt.title("Median"); plt.imshow(median)
plt.subplot(2, 3, 5); plt.title("Bilateral"); plt.imshow(bilateral)

plt.show()
