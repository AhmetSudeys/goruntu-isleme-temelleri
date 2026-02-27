# Hafta 2: Akıllı Trafik Kamerası - Veri Artırımı ve Geometrik Dönüşümler

<img width="1573" height="591" alt="Ekran görüntüsü 2026-02-27 235908" src="https://github.com/user-attachments/assets/ce749592-38bd-4c66-9d9e-237c00467989" />

Bu klasör, "Akıllı Trafik Kamerası" yapay zeka modellerini eğitmek amacıyla kullanılan veri artırımı (data augmentation) ve ileri seviye geometrik dönüşüm tekniklerini içerir.

## Senaryo
Yapay zeka modelinin farklı açılardan, uzaklıklardan ve hava koşullarından gelen araç görüntülerini doğru tanıyabilmesi için mevcut veri setinin çoğaltılması gerekmektedir. Bu projede, araç görüntülerine gerçek dünya senaryolarını simüle eden Affin dönüşümleri uygulanarak veri çeşitliliği artırılmıştır.



## Gerçekleştirilen İşlemler

### 1. Görüntü Analizi ve Çözünürlük
İşlem öncesinde görüntünün matris boyutları ve DPI (çözünürlük) değerleri analiz edilerek ekrana yazdırılmıştır. Bu adım, model eğitiminde kullanılacak verinin standartlara uygunluğunu denetlemek için uygulanır.

### 2. Affin Dönüşüm Matrisi Hazırlığı
Görüntüye aynı anda birden fazla perspektif etkisi kazandırmak için karmaşık bir Affin matrisi oluşturulmuştur:
- **%20 Büyütme (Scale):** Aracın kameraya olan mesafesi simüle edilmiştir.
- **30 Derece Döndürme (Rotation):** Kameranın farklı açılardan bakış açısı uygulanmıştır.
- **Yatay Kayma (Shear x:0.2):** Rüzgar efekti veya perspektif bozulması eklenmiştir.
- **Öteleme (Translation):** Aracın şerit içindeki farklı konumları simüle edilmiştir.

### 3. Sınır Hesaplama ve İnterpolasyon
Dönüşüm sonrası görüntünün kesilmemesi ve sınır taşması yaşanmaması için yeni çerçeve boyutları dinamik olarak hesaplanmıştır. Görüntü kalitesini korumak adına **Bilineer İnterpolasyon** yöntemi kullanılarak pikseller yeniden yapılandırılmıştır.



## Klasör İçeriği
* AkilliTrafikKamerasi.py: Affin dönüşümlerini ve sınır hesaplamalarını içeren ana Python kodu.
* img1.jpg: Dönüşüm uygulanan orijinal araç görüntüsü.

## Çalıştırma
Gerekli kütüphaneleri (OpenCV, NumPy, Matplotlib) kurduktan sonra terminale şu komutu yazarak projeyi çalıştırabilirsiniz:

```bash
python TrafikVeriArtirimi.py

