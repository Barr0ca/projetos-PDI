import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. Carregar imagem
image = cv2.imread("../images/gon.png")  # OpenCV carrega em BGR
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 2. Compressão JPEG

# JPEG qualidade alta
cv2.imwrite(
    "imagem_jpeg_90.jpg",
    image,
    [cv2.IMWRITE_JPEG_QUALITY, 90]
)

# JPEG qualidade baixa
cv2.imwrite(
    "imagem_jpeg_20.jpg",
    image,
    [cv2.IMWRITE_JPEG_QUALITY, 20]
)

# 3. Função para tamanho do arquivo
def Tamanho(nome):
    bytes = os.path.getsize(nome)
    return bytes / 1024


print("Tamanho dos arquivos (KB)")
print("PNG:", Tamanho("../images/gon.png"))
print("JPEG qualidade 90:", Tamanho("imagem_jpeg_90.jpg"))
print("JPEG qualidade 20:", Tamanho("imagem_jpeg_20.jpg"))

# 4. Descompressão
jpeg90 = cv2.imread("imagem_jpeg_90.jpg")
jpeg90 = cv2.cvtColor(jpeg90, cv2.COLOR_BGR2RGB)

jpeg20 = cv2.imread("imagem_jpeg_20.jpg")
jpeg20 = cv2.cvtColor(jpeg20, cv2.COLOR_BGR2RGB)

# 5. Visualização
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title("Original PNG")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(jpeg90)
plt.title("JPEG qualidade 90")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(jpeg20)
plt.title("JPEG qualidade 20")
plt.axis("off")

plt.show()

# 6. Erro de reconstrução MSE
def mse(img1,img2):
    return np.mean((img1-img2)**2)

erro90 = mse(image_rgb.astype(float), jpeg90.astype(float))
erro20 = mse(image_rgb.astype(float), jpeg20.astype(float))
print("\nErro MSE JPEG 90:", erro90)
print("Erro MSE JPEG 20:", erro20)