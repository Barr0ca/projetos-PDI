# Exemplo sobre Amostragem e Quantização

# Bibliotecas
import cv2
import numpy as np

# Carregando a imagem
img = cv2.imread("lobo.jpg", cv2.IMREAD_COLOR)
num_cinza = 8 # Níveis de cinza por canal
levels = np.linspace(0, 255, num_cinza, endpoint=True).astype(np.uint8)

# Método
def quantizar_uniforme(img, num_cinza):
    bins = 250 // num_cinza
    q = (img // bins) * bins + bins // 2

    return q.astype(np.uint8)

quant = quantizar_uniforme(img, num_cinza)
cv2.imwrite("lobo_quant_unif.jpg", quant)

# Quantizar com K-means
Z = img.reshape((-1,3)).astype(np.float32)
num_cores = 16 # Número de cores da paleta

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
_, labels, centers = cv2.kmeans(Z, num_cores, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
quant = centers[labels.flatten()].reshape(img.shape)
cv2.imwrite("lobo_quant_kmeans16.jpg", quant)

#  Amostragem
altura, largura = img.shape[:2]

# Downsample
down = cv2.resize(img, (largura//2, altura//2), interpolation=cv2.INTER_AREA)
cv2.imwrite("lobo_down_2x.png", down)

# Upsample
up = cv2.resize(img, (largura*2, altura*2), interpolation=cv2.INTER_NEAREST)
cv2.imwrite("lobo_up_2x.png", up)

