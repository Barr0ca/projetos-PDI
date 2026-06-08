import cv2
import numpy as np

pixels = {"P1": [255, 0,   0],
          "P2": [120, 180, 90],
          "P3": [50,  50,  200]}

for nome, rgb in pixels.items():

    img = np.uint8([[[rgb[2], rgb[1], rgb[0]]]])  # Converte para BGR

    h, s, v = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)[0, 0]  # Converte para HSV

    print(nome, f"H={h*2}°", f"S={s/255*100:.1f}%",
          f"V={v/255*100:.1f}%")  # Exibe os valores de H, S e V

# A) Converte RGB → BGR → HSV (OpenCV) e exibe H (×2 → °), S e V (÷255 → %).

# B) H = tipo de cor; S = pureza (0% = cinza); V = brilho.
# P1 (0°, 100%, 100%): vermelho puro, máximo brilho e saturação.
# P2 (~100°, ~50%, ~71%): verde-amarelado, cor moderada, brilho médio-alto.
# P3 (240°, 75%, ~78%): azul saturado, brilho alto.

# C) Em RGB, cor e iluminação estão misturadas nos 3 canais; em HSV, H isola a cor,
# S e V separam pureza e brilho. Assim, segmentar por faixa de H é mais simples e
# mais robusto a mudanças de luz do que combinar limites em R, G e B.
