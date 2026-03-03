import cv2
import numpy as np
import matplotlib.pyplot as plt

def manual_mean_filter(image, kernel_size=5):
    pad = kernel_size // 2
    padded_img = np.pad(image, pad, mode='reflect')
    output = np.zeros_like(image, dtype=np.float32)
    
    kernel_area = kernel_size * kernel_size
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_img[i:i+kernel_size, j:j+kernel_size]
            output[i, j] = np.sum(region) / kernel_area
            
    return np.uint8(output)

def manual_median_filter(image, kernel_size=3):
    pad = kernel_size // 2
    padded_img = np.pad(image, pad, mode='reflect')
    output = np.zeros_like(image, dtype=np.uint8)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_img[i:i+kernel_size, j:j+kernel_size]
            output[i, j] = np.median(region)
            
    return output

def get_gaussian_kernel(size=5, sigma=1):
    kernel = np.zeros((size, size), dtype=np.float32)
    center = size // 2
    
    sum_val = 0.0
    for i in range(size):
        for j in range(size):
            x = i - center
            y = j - center
            # 2B Gaussian denklemi
            kernel[i, j] = (1 / (2 * np.pi * sigma**2)) * np.exp(-(x**2 + y**2) / (2 * sigma**2))
            sum_val += kernel[i, j]
            
    return kernel / sum_val

def manual_gaussian_filter(image, kernel_size=5, sigma=1):
    kernel = get_gaussian_kernel(kernel_size, sigma)
    pad = kernel_size // 2
    padded_img = np.pad(image, pad, mode='reflect')
    output = np.zeros_like(image, dtype=np.float32)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_img[i:i+kernel_size, j:j+kernel_size]
            output[i, j] = np.sum(region * kernel)
            
    return np.uint8(output)


# Görüntüyü gri tonlamalı olarak okuyoruz
img = cv2.imread('img1.png', 0)

if img is None:
    print("dosya bulunamadı hatası var")
else:
    print("lütfen bekleyiniz")
    
    mean_filtered_img = manual_mean_filter(img, kernel_size=5)
    median_filtered_img = manual_median_filter(img, kernel_size=3)
    gaussian_filtered_img = manual_gaussian_filter(img, kernel_size=5, sigma=1)

    # GÖRÜNTÜ ÇİZİMLERİ
    plt.figure(figsize=(12, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Orijinal Gürültülü Görüntü')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(mean_filtered_img, cmap='gray')
    plt.title('Manuel Ortalama Filtre (5x5)')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(median_filtered_img, cmap='gray')
    plt.title('Manuel Medyan Filtre (3x3)')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(gaussian_filtered_img, cmap='gray')
    plt.title('Manuel Gaussian Filtresi (5x5, sigma=1)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    # HİSTOGRAM ÇİZİMLERİ
    plt.figure(figsize=(18, 10))

    plt.subplot(2, 2, 1)
    plt.title('Orijinal Görüntü Histogramı')
    plt.hist(img.ravel(), 256, range=[0, 256])
    plt.xlabel('Piksel Yoğunluğu')
    plt.ylabel('Piksel Sayısı')
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.title('Manuel Ortalama Filtre (5x5) Histogramı')
    plt.hist(mean_filtered_img.ravel(), 256, range=[0, 256])
    plt.xlabel('Piksel Yoğunluğu')
    plt.ylabel('Piksel Sayısı')
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.title('Manuel Medyan Filtre (3x3) Histogramı')
    plt.hist(median_filtered_img.ravel(), 256, range=[0, 256])
    plt.xlabel('Piksel Yoğunluğu')
    plt.ylabel('Piksel Sayısı')
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.title('Manuel Gaussian Filtre (5x5, sigma=1) Histogramı')
    plt.hist(gaussian_filtered_img.ravel(), 256, range=[0, 256])
    plt.xlabel('Piksel Yoğunluğu')
    plt.ylabel('Piksel Sayısı')
    plt.grid(True)

    plt.tight_layout()
    plt.show()