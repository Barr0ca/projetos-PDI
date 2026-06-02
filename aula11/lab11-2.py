import cv2
import matplotlib.pyplot as plt

# Carregar a imagem
image = cv2.imread('casas.jpg', 0)

# Aplica pseudocores usando um mapa de cores
pseudo = cv2.applyColorMap(image, cv2.COLORMAP_JET)

# Converter BGR em RGB
pseudo = cv2.cvtColor(pseudo, cv2.COLOR_BGR2RGB)

# Exibição
plt.figure(figsize=(10, 5))

plt.subplot(1,2,1); plt.imshow(image, cmap='gray'); plt.title('Imagem Original'); plt.axis('off')
plt.subplot(1,2,2); plt.imshow(pseudo); plt.title('Codificação de Cores JET'); plt.axis('off')

plt.show()