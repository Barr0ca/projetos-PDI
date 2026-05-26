# Aplicação de ruído sal e pimenta e restauração com mediana

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image = cv2.imread('netero.jpg', 0)

# Criar ruído sal e pimenta
noise_prob = 0.05
noisy_image = np.copy(image)

# Ruído sal
salt = np.random.rand(*image.shape) < noise_prob
noisy_image[salt] = 255

# Ruído pimenta
pepper = np.random.rand(*image.shape) < noise_prob
noisy_image[salt] = 0

# Restauração com filtro de mediana
restored_image = cv2.medianBlur(noisy_image, 3)

# Exibir resultados
titles = ['Original', 'Ruído sal e pimenta', 'Restaurada']
images = [image, noisy_image, restored_image]

plt.figure(figsize=(12,4))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap='inferno')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()