import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
img = cv2.imread('../images/rebanho.png', cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.uint8)

# Montar imagem original
plt.figure(figsize=(6, 6))
plt.imshow(img, cmap='gray')
plt.title("imagem original")
plt.axis("off")
plt.show()

# Calcular redundância interpixel: diferença entre pixels vizinhos
diferenca = np.zeros_like(img, dtype=int)

for y in range(img.shape[0]):
    for x in range(1, img.shape[1]):
        diferenca[y, x] = (int(img[y, x]) - int(img[y, x-1]))

# Deslocamento para visualização
diferenca_visual = diferenca + 128

# Mostrar imagem diferencial
plt.figure(figsize=(6, 6))
plt.imshow(diferenca_visual, cmap='gray')
plt.title("imagem após diferenca visual\n(redundância visual)")
plt.axis("off")
plt.show()

# Histogramas
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(diferenca.ravel(), bins=256)
plt.title("Histograma imagem diferencial")
plt.show()

# Medir quantidade de valores repetidos
unique_original = len(np.unique(img))
unique_diferenca = len(np.unique(diferenca))
