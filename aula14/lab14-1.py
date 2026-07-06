import cv2
from collections import Counter
from arithmetic_compressor import AECompressor

imagem = cv2.imread("netero.jpg", cv2.IMREAD_GRAYSCALE)

dados = imagem.flatten().tolist()

freq = Counter(dados)

modelo = {}

total = sum(freq.values())

for k, v in freq.items():
    modelo[k] = v / total

compressor = AECompressor(modelo)
codigo = compressor.compress(dados)

print("Quantidade de símbolos:", len(dados))
print("Tamanho da sequência comprimida:", len(codigo))
