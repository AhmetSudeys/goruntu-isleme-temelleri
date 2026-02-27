# Hafta 1: Otonom Tarım Dronu - Görüntü İyileştirme ve Analiz

Bu klasör, otonom tarım dronlarının sabah saatlerinde karşılaştığı düşük ışık, sis ve düşük kontrast problemlerini çözmek amacıyla geliştirilen temel görüntü işleme tekniklerini içerir.

## Senaryo
Dronlar tarafından çekilen bitki fotoğrafları, hava koşulları nedeniyle sisli ve düşük kontrastlıdır. Yapay zeka modellerinin bitki hastalıklarını doğru teşhis edebilmesi için görüntülerin hem görsel kalitesinin artırılması hem de RGB'den HSV (Hue, Saturation, Value) renk uzayına dönüştürülerek analiz edilmesi gerekmektedir.

## Gerçekleştirilen İşlemler

### 1. Histogram Analizi
Tarladan alınan karanlık görüntünün gri tonlamalı piksel dağılımı analiz edilmiştir. Bu analiz, görüntünün hangi yoğunluk aralığında sıkıştığını belirlemek için kritik öneme sahiptir.

### 2. Kontrast İyileştirme (CLAHE)
Bölgesel detayları (bitki yapraklarını ve damarlarını) ortaya çıkarmak için Contrast Limited Adaptive Histogram Equalization (CLAHE) algoritması uygulanmıştır. Standart eşitlemeye göre gürültüyü sınırlayarak daha doğal bir keskinlik sağlar.

### 3. Renk Uzayı Dönüşümü (RGB -> HSV)
Yapay zeka modelinin renk analizini (bitki sağlığı tespiti vb.) daha sağlıklı yapabilmesi için görüntüler matematiksel formüller kullanılarak HSV renk uzayına dönüştürülmüştür:

- **Hue (Renk Özü):** Rengin türünü belirler.
- **Saturation (Doygunluk):** Rengin canlılığını belirler.
- **Value (Parlaklık):** Işık yoğunluğunu belirler.

## Klasör İçeriği
* BitkiAnaliz.py: Tüm görüntü işleme adımlarını içeren ana Python kodu.
* img1.jpeg: Analiz edilen orijinal tarla/bitki görüntüsü.

## Çalıştırma
Gerekli kütüphaneleri (OpenCV, NumPy, Matplotlib) kurduktan sonra terminale şu komutu yazarak projeyi çalıştırabilirsiniz:

```bash
python BitkiAnaliz.py
