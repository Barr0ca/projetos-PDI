import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
img = cv2.imread('../images/cores.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Definir cor-alvo: verde (green)
target = np.array([0, 255, 0])

# Calcular distância euclidiana
dist = np.sqrt(np.sum((img - target)**2, axis=2))

# Threshold
T = 100

result = img.copy()

# Converte pixel não selecionados para escala de cinza:
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_rgb = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)

result[dist > T] = gray_rgb[dist > T]

# Exibir resultados:
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1); plt.imshow(img); plt.title('Original'); plt.axis('off')
plt.subplot(1, 2, 2); plt.imshow(result); plt.title('Fatiamento'); plt.axis('off')
plt.show()
