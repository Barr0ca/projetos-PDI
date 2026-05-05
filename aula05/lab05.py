# Histogramas
import matplotlib.pyplot as plt
import cv2

# Carregar imagem
img = cv2.imread("lobo.jpg")

# Histograma em escala de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Imagem equalizada
img_equalized = cv2.equalizeHist(img_gray)

# Imagem em tons de cinza
plt.subplot(2, 2, 1), plt.imshow(img_gray, cmap="gray")
plt.axis("off")
plt.title("Grayscale")

# Gráfico do histograma (PIXELS x INTENSIDADE)
plt.subplot(2, 2, 2), plt.hist(img_gray.ravel(), 256, [0, 256], color="k")
plt.title("Gray Histogram")

# Imagem em tons de cinza equalizada
plt.subplot(2, 2, 3), plt.imshow(img_equalized, cmap="gray")
plt.axis("off")
plt.title("Equalized")

# Gráfico do histograma equalizado (PIXELS x INTENSIDADE)
plt.subplot(2, 2, 4), plt.hist(img_equalized.ravel(), 256, [0, 256], color="k")
plt.title("Equalize Histogram")

# for i, c in enumerate(('r','g','b')):
#     plt.plot(cv2.calcHist([img], [i], None, [256], [0, 256]), color=c)
# plt.title("Histograma RGB")
# plt.xlabel("Intensidade"), plt.ylabel("Frequência")

plt.show()
