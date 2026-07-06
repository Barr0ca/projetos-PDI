import cv2
import heapq
from collections import Counter

# Leitura da imagem
imagem = cv2.imread('gon.png', cv2.IMREAD_GRAYSCALE)
pixels = imagem.flatten()

# Frequência dos símbolos
frequencias = Counter(pixels)

# Construção da árvore de Huffman
heap = [[peso, [simbolo, ""]] for simbolo, peso in frequencias.items()]

heapq.heapify(heap)

while len(heap) > 1:
    menor = heapq.heappop(heap)
    maior = heapq.heappop(heap)
    for par in menor[1:]:
        par[1] = '0' + par[1]
    for par in maior[1:]:
        par[1] = '1' + par[1]
    heapq.heappush(heap, [menor[0] + maior[0]] + menor[1:] + maior[1:])

codigo = sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))
tabela = dict(codigo)
bits = ""

for p in pixels:
    bits += tabela[p]

bits_originais = len(pixels) * 8
bits_huffman = len(bits)

print("Bits originais:", bits_originais)
print("Bits após Huffman:", bits_huffman)
print("Taxa de compressão:", bits_originais / bits_huffman)
