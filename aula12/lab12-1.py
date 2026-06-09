import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
img = cv2.imread('../images/rebanho.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Converte RGB para HSV
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# Especificar limites da cor Verde
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

# Máscara de segmentação
mask = cv2.inRange(hsv, lower_green, upper_green)

# Aplicar a máscara:
segmented = cv2.bitwise_and(img, img, mask=mask)

# Exibir resultados:
plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1); plt.imshow(img); plt.title('Original'); plt.axis('off')
plt.subplot(1, 3, 2); plt.imshow(mask); plt.title('Máscara'); plt.axis('off')
plt.subplot(1, 3, 3); plt.imshow(segmented); plt.title('Segmentado'); plt.axis('off')
plt.show()
