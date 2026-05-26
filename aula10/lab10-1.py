# Aplicação de filtragem inversa
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import wiener

# Carregar a imagem
image = cv2.imread('netero.jpg', 0)

# Criar Kernel de desfoque de movimento
size = 15
kernel = np.zeros((size, size))
kernel[int((size - 1) / 2), :] = np.ones(size)
kernel = kernel / size

# Aplicar degradação
blurred = cv2.filter2D(image, -1, kernel)

# Transformada de Fourier

F_blurred = np.fft.fft2(blurred)
H = np.fft.fft2(kernel, s=image.shape)

# Evitar divisão por 0
epsilion = 1e-3
H = H + epsilion

# Filtragem inversa
F_restored = F_blurred / H # no domínio da frequência
restored = np.abs(np.fft.ifft2(F_restored)) # volta ao domínio do espaço 

# Normalizar
restored = np.clip(restored, 0, 255).astype(np.uint8)

restored = wiener(blurred, (15, 15))

# Exibir resultados
titles = ['Original', 'Desfoque de Movimento', 'Restaurada']
images = [image, blurred, restored]

plt.figure(figsize=(12,4))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap='inferno')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()


