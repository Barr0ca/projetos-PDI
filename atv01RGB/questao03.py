import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Carregar imagem colorida
image_bgr = cv2.imread('gon.png')
image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# 2. Converter para HSV
hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
hsv_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)  # visualização da imagem HSV

# 3. Limiares para a cor verde (OpenCV: H=0–179; verde ≈ 35–85)
lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])

# 4. Máscara binária
mask = cv2.inRange(hsv, lower_green, upper_green)

# 5. Resultado segmentado
segmented = cv2.bitwise_and(image_bgr, image_bgr, mask=mask)
segmented = cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB)

# Exibição
plt.figure(figsize=(14, 4))
plt.subplot(1, 4, 1); plt.imshow(image); plt.title('Original'); plt.axis('off')
plt.subplot(1, 4, 2); plt.imshow(hsv_rgb); plt.title('HSV'); plt.axis('off')
plt.subplot(1, 4, 3); plt.imshow(mask, cmap='gray'); plt.title('Máscara'); plt.axis('off')
plt.subplot(1, 4, 4); plt.imshow(segmented); plt.title('Segmentado'); plt.axis('off')
plt.tight_layout()
plt.show()

# A) HSV separa matiz (cor) de saturação e valor (brilho), facilitando limiarização por faixa de H.

# B) Mudanças de iluminação alteram V e S; áreas escuras/claras podem sair da faixa e ser
#    excluídas ou incluídas incorretamente na máscara.

# C) Pré-processamento: equalização do canal V (ou normalização de iluminação) antes da
#    segmentação, para reduzir variação de brilho entre regiões verdes.
