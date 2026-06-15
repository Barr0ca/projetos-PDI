import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image = cv2.imread('casas.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Imagem separada nos 3 canais
R = image[:,:,0]
G = image[:,:,1]
B = image[:,:,2]

# Exibir RGB
plt.figure(figsize=(12,4))
plt.subplot(1,4,1); plt.imshow(image); plt.title('Imagem RGB'); plt.axis('off')
plt.subplot(1,4,2); plt.imshow(R); plt.title('Red'); plt.axis('off')
plt.subplot(1,4,3); plt.imshow(G); plt.title('Green'); plt.axis('off')
plt.subplot(1,4,4); plt.imshow(B); plt.title('Blue'); plt.axis('off')
plt.show()

def rgb_to_hsi(image):
    image = image.astype(np.float32) / 255.0

    R = image[:,:,0]
    G = image[:,:,1]
    B = image[:,:,2]

    numerator = 0.5 * ((R - G) + (R - B))
    denominator = np.sqrt((R - G)**2 + (R - B)*(G - B))

    theta = np.arccos(np.clip(numerator / (denominator + 1e-8), -1, 1))

    H = np.where(B <= G, theta, 2*np.pi - theta)
    H = H / (2*np.pi)

    min_rgb = np.minimum(np.minimum(R, G), B)
    S = 1 - (3 / (R + G + B + 1e-8)) * min_rgb

    I = (R + G + B) / 3
    return H, S, I

rgb_to_hsi(image)