# Hafta 4: Otonom Araç Görüş Sistemi - Kenar Algılama ve Frekans Analizi

<img width="1606" height="938" alt="image" src="https://github.com/user-attachments/assets/ae911d82-f0e2-446e-82d9-dedbd298e3bc" />


Bu klasör, otonom araç yazılımlarında yol şeritlerinin tespiti, tabela sınırlarının belirlenmesi ve kamera sensörlerinden kaynaklanan periyodik gürültülerin analizi için kullanılan ileri seviye görüntü işleme tekniklerini içerir.

## Senaryo
Geliştirdiğimiz otonom araç yazılımının güvenli sürüş yapabilmesi için yolu ve çevresini yüksek doğrulukla "anlaması" gerekmektedir. Bu projede, şerit ve tabela sınırlarını netleştirmek için **Gradyan Analizi** uygulanmış; kameradaki elektriksel parazitleri tespit etmek amacıyla da görüntünün **Frekans Bileşenleri** analiz edilmiştir.

## Gerçekleştirilen İşlemler

### 1. Gradyan Analizi (Sobel Filtresi)
Yol görüntüsündeki dikey şeritleri ve yatay tabela sınırlarını yakalamak için Sobel operatörü kullanılmıştır. 
- **Yatay ve Dikey Türev:** Görüntünün $x$ ve $y$ yönlerindeki yoğunluk değişimleri ($G_x$ ve $G_y$) hesaplanmıştır.
- **Gradyan Büyüklüğü:** Kenarları yön bağımsız hale getirmek ve belirginleştirmek için şu formül uygulanmıştır:
  $$G = \sqrt{G_x^2 + G_y^2}$$

### 2. Kenar Karşılaştırma: Sobel ve Laplacian
Farklı matematiksel yaklaşımların kenar tespitindeki başarısı görsel olarak kıyaslanmıştır:
- **Sobel:** Birinci türevi temel alır, gürültüye karşı daha dayanıklıdır ve kenar yönünü tayin edebilir.
- **Laplacian:** İkinci türevi kullanır, tüm yönlerdeki kenarları (isotropic) tek seferde yakalar ancak gürültüye karşı daha hassastır.

### 3. Frekans Analizi (Ayrık Fourier Dönüşümü - DFT)
Kameradaki elektriksel parazitleri ve periyodik desenleri analiz etmek için görüntü uzaysal boyuttan frekans boyutuna taşınmıştır:
- **DFT ve Spektrum:** Görüntünün frekans haritası çıkarılmış ve **Magnitude Spectrum** oluşturulmuştur.
- **Merkezleme (Shift):** Analizi kolaylaştırmak için düşük frekans bileşenleri görüntünün merkezine taşınarak spektrumun merkezlenmiş hali ekrana çizdirilmiştir.



## Klasör İçeriği
* OtonomGorusSistemi.py: Sobel, Laplacian ve DFT analizlerini içeren ana Python kodu.
* yol_test.jpg: Analizlerin uygulandığı orijinal yol ve tabela görüntüsü.

## Çalıştırma
Gerekli kütüphaneleri (OpenCV, NumPy, Matplotlib) kurduktan sonra terminale şu komutu yazarak projeyi çalıştırabilirsiniz:

```bash
python OtonomGorusSistemi.pyy
