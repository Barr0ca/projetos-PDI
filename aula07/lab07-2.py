# Filtro Passa-Alta

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('casas.jpg', 0)

# Transformada de Fourier
dft = np.fft.fft2(image)
dft_shift = np.fft.fftshift(dft)
rows, cols = image.shape
crow, ccol = rows//2, cols//2

# Criar máscara
mask = np.ones((rows, cols), np.uint8)
radius = 60
for i in range(rows):
    for j in range(cols):
        if (i-crow)**2 + (j-ccol)**2 <= radius**2:
            mask[i,j] = 0  

# Aplicar filtro
filtered = dft_shift * mask

# Transformada inversa
f_ishift = np.fft.ifftshift(filtered)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# Mostrar
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.imshow(image, cmap='gray')
plt.title('Original')
plt.subplot(1,2,2)
plt.imshow(img_back, cmap='gray')
plt.title('Filtro Passa-Alta')

plt.show()