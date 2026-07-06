import cv2

imagem = cv2.imread("gon.png", cv2.IMREAD_GRAYSCALE)
dados = imagem.flatten().tolist()
dados = ''.join(chr(x) for x in dados)

# Compressão LZW
dicionario = {chr(i): i for i in range(256)}
codigo = []
p = ""
indice = 256

for c in dados:
    pc = p + c
    if pc in dicionario:
        p = pc
    else:
        codigo.append(dicionario[p])
        dicionario[pc] = indice
        indice += 1
        p = c

if p:
    codigo.append(dicionario[p])

print("Quantidade de códigos:", len(codigo))
print("Tamanho do dicionário:", len(dicionario))