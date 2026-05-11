# Transformada Discreta de Furrier

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ler imagem em escala de cinza
image = cv2.imread('casas.jpg', 0)

# Calcular Transformada de Fourier
dft = np.fft.fft2(image)

# Mover baixas frequências para o centro
dft_shift = np.fft.fftshift(dft)

# Espectro de magnitude
magnitude = 20 * np.log(np.abs(dft_shift) + 1)


# Exibir
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(image, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(magnitude, cmap='gray')
plt.title('Espectro de Frequência')
plt.axis('off')

plt.show()