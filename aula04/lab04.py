import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Carregar imagem
    image = cv2.imread('gon.png', cv2.IMREAD_GRAYSCALE)

    # Normalizar a imagem para as intensidades ficarem entre [0, 1]
    image = image / 255.0

    # Criar uma máscara (mesmo tamanho)
    mask = np.zeros_like(image)

    # Definir uma região (ROI) retangular
    h, w = image.shape
    mask[int(h*0.3):int(h*0.7), int(w*0.3):int(w*0.7)] = 1

    # Aplicar a máscara usando a multiplicação pela imagem
    result = image * mask

    # Plotar os resultados
    plt.figure(figsize=(10,4))

    plt.subplot(1, 3, 1)
    plt.title('Imagem Original')
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title('Máscara')
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title('Resultado Mascarado')
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    cv2.imwrite(image)

if __name__ == "__main__":
    main()
