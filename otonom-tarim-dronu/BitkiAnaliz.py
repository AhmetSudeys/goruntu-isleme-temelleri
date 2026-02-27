
import cv2
import numpy as np
import matplotlib.pyplot as plt


img_bgr =  cv2.imread('img1.jpeg')

if img_bgr is None:
    print("Hata: Dosya yolu yanlış veya resim bulunamadı! Lütfen yolu kontrol et.")
else:
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    img_enhanced = clahe.apply(img_gray)

    def rgb_to_hsv_manual(img):
        rgb = img.astype(np.float32) / 255.0
        R, G, B = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
        Cmax = np.max(rgb, axis=2)
        Cmin = np.min(rgb, axis=2)
        delta = Cmax - Cmin
        V = Cmax
        S = np.where(Cmax == 0, 0, delta / Cmax)
        H = np.zeros_like(Cmax)
        mask = delta != 0
        H[mask & (Cmax == R)] = 60 * (((G - B) / delta) % 6)[mask & (Cmax == R)]
        H[mask & (Cmax == G)] = 60 * (((B - R) / delta) + 2)[mask & (Cmax == G)]
        H[mask & (Cmax == B)] = 60 * (((R - G) / delta) + 4)[mask & (Cmax == B)]
        return H, S, V

    H, S, V = rgb_to_hsv_manual(img_rgb)

    plt.figure(figsize=(16, 8))

    plt.subplot(2, 3, 1); plt.imshow(img_rgb); plt.title("1. Orijinal (Sisli/Karanlık)")
    plt.subplot(2, 3, 4); plt.hist(img_gray.ravel(), 256, [0, 256], color='gray')
    plt.title("Orijinal Histogram")

    plt.subplot(2, 3, 2); plt.imshow(img_enhanced, cmap='gray'); plt.title("2. CLAHE (İyileştirilmiş)")
    plt.subplot(2, 3, 5); plt.hist(img_enhanced.ravel(), 256, [0, 256], color='blue')
    plt.title("Yeni Histogram (Yayılmış)")

    plt.subplot(2, 3, 3); plt.imshow(H, cmap='hsv'); plt.title("3. Renk Özü (Hue Channel)")

    plt.tight_layout()
    plt.show()
    print("Analiz başarıyla tamamlandı!")
