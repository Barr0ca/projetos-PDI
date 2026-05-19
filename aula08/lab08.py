import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Carregar imagem
image = cv2.imread("netero.jpg", 0)

# 2. Criar degradação por blur com
# Gaussian blur simula degradação óptica
blurred = cv2.GaussianBlur(image, (11, 11), 5)

# 3. Criar ruído Gaussiano
mean = 0
std = 25
noise = np.random.normal(mean, std, image.shape)

# Adicionar ruído à imagem original
noisy = image + noise

# Limitar valores ao intervalo válido da imagem
noisy = np.clip(noisy, 0, 255).astype(np.uint8)

# 4. Blur + ruído
blurred_noisy = blurred + noise
blurred_noisy = np.clip(blurred_noisy, 0, 255).astype(np.uint8)

# 5. Exibir resultados
titles = ["Imagem Original", "Imagem Borrada", "Imagem com Ruído", "Imagem Borrada + Ruído"]
images = [image, blurred, noisy, blurred_noisy]

# Exibir
plt.figure(figsize=(12, 8))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()