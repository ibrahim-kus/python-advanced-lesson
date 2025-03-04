import cv2
import numpy as np

# Görseli yükle
image = cv2.imread("kalp.png")

# Görseli griye çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kenarları tespit et (Canny Algoritması)
edges = cv2.Canny(gray, 50, 150)

# Beyaz arka plan oluştur
white_bg = np.ones_like(image) * 255

# Kenarları beyaz arka plana yerleştir
white_bg[edges > 0] = (0, 0, 0)

# Sonucu kaydet
cv2.imwrite("kalp-black-white.png", white_bg)

# Görüntüyü göster
cv2.imshow("Result", white_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()