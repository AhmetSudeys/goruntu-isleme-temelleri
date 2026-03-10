# improt işlemleri
import cv2
import numpy as np
from matplotlib import pyplot as plt

# resmi doğrudan gri tonda okutuyorum
img = cv2.imread('road.jpg', 0)

# dikey kenarları bulmak için x ekseninde sobel uyguladım
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# yatay kenarları bulmak için y ekseninde sobel uyguladım
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# x ve y gradyanlarını pisagorla birleştirip toplam büyüklüğü hesapladım
sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)
# görüntüyü ekrana basabilmek için 8 bitlik formata geri çevirdim
sobel_final = np.uint8(sobel_combined)

# tüm yönlerdeki kenarları tekte yakalamak için laplacian filtresi kullandım
laplacian = cv2.Laplacian(img, cv2.CV_64F)
# negatif değerleri mutlak değerle düzeltip yine 8 bite aldım
laplacian_final = np.uint8(np.absolute(laplacian))

# resmin fourier dönüşümünü alıp frekans uzayına geçtim
dft = np.fft.fft2(img)
# düşük frekans bileşenleri merkezde toplansın diye shift işlemi yaptım
dft_shift = np.fft.fftshift(dft) 

# detayları ekranda seçebilmek için genlik spektrumunu logaritmik hale getirdim
magnitude_spectrum = 20 * np.log(np.abs(dft_shift))

# çizim yapacağım pencerenin boyutunu ayarladım
plt.figure(figsize=(10, 8))

# 2x2'lik gridin ilk kısmına orijinal resmi gri tonda yerleştirdim
plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
# başlığını yazıp kenardaki eksen rakamlarını sildim
plt.title('Orijinal'), plt.xticks([]), plt.yticks([])

# gridin ikinci kısmına hesapladığım sobel görüntüsünü koydum
plt.subplot(2, 2, 2), plt.imshow(sobel_final, cmap='gray')
# başlığı ekleyip eksenleri gizledim
plt.title('Sobel'), plt.xticks([]), plt.yticks([])

# üçüncü kısma laplacian sonucunu ekledim
plt.subplot(2, 2, 3), plt.imshow(laplacian_final, cmap='gray')
# başlığı atıp yine eksenleri temizledim
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

# son kısma da fourier spektrumunu yerleştirdim
plt.subplot(2, 2, 4), plt.imshow(magnitude_spectrum, cmap='gray')
# başlığı yazıp eksenleri kapattım
plt.title('DFT Spektrum'), plt.xticks([]), plt.yticks([])

# grafikler birbirine yapışmasın diye boşlukları otomatik ayarlattım
plt.tight_layout()
# hazırladığım tüm çizimleri ekranda gösteriyorum
plt.show()