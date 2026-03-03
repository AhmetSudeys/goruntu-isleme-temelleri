# Hafta 3: Röntgen Filtreleme - Biyomedikal Görüntü Gürültü Giderme

<div align="center">
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/4f6f9908-0a1e-483b-9920-d933ba762dd9" alt="Orijinal Gürültülü Görüntü">
      <p><b>Orijinal Gürültülü Görüntü</b></p>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/738a0498-5539-4a55-9fa1-d0a0142d2e65" alt="Tüm Filtrelerin Karşılaştırmalı Sonuçları">
      <p><b>Tüm Filtrelerin Karşılaştırmalı Sonuçları (Grid)</b></p>
    </td>
  </tr>
</table>
</div>

Bu klasör, biyomedikal görüntüleme sistemlerinden elde edilen röntgen görüntülerindeki iletim hattı parazitlerini ve gürültüleri gidermek amacıyla geliştirilen temel uzamsal filtreleme tekniklerini içerir.

## Senaryo
Bir biyomedikal görüntüleme sisteminden gelen röntgen görüntülerinde, iletim hattındaki parazitler nedeniyle yoğun gürültü oluşmuştur. Bu gürültüler, doktorların doku kenarlarını net görmesini ve doğru teşhis koymasını engellemektedir. Sorunu çözmek ve görüntü detaylarını iyileştirmek için farklı filtreleme yöntemleri karşılaştırmalı olarak uygulanmıştır.

## Gerçekleştirilen İşlemler

### 1. Ortalama (Mean) Filtresi
Görüntüdeki genel gürültüyü azaltmak amacıyla 5x5 boyutunda bir aritmetik ortalama filtresi uygulanmıştır. Bu işlem, her pikselin değerini komşularının ortalaması ile değiştirerek genel bir yumuşatma sağlar ancak kenar keskinliğini bir miktar azaltır.

### 2. Medyan (Median) Filtresi
Özellikle parazitli gürültüleri temizlemek için 3x3 boyutunda bir medyan filtresi uygulanmıştır. Bu yöntemde piksellerin medyan değeri alındığı için, ortalama filtreye kıyasla doku kenarları ve yapısal hatlar çok daha başarılı bir şekilde korunmuştur.

### 3. Gaussian Filtresi
Görüntüye daha doğal ve ağırlıklı bir yumuşatma etkisi vermek için sigma = 1 değeri ile 5x5 boyutunda bir Gaussian filtresi uygulanmıştır. Bu filtre ile gürültü azaltılırken merkeze yakın piksellere daha fazla ağırlık verilerek ortalama filtreye göre daha dengeli bir sonuç elde edilmiştir.

## Klasör İçeriği
* RontgenAnaliz.py: Tüm filtreleme adımlarını ve kıyaslamaları içeren ana Python kodu.
* rontgen.jpeg: Analiz edilen orijinal, gürültülü biyomedikal röntgen görüntüsü.

## Çalıştırma
Gerekli kütüphaneleri (OpenCV, NumPy, Matplotlib) kurduktan sonra terminale şu komutu yazarak projeyi çalıştırabilirsiniz:

```bash
python RontgenAnaliz.py
