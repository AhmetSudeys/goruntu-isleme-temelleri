import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


#-----------------------------------------------------------------------------

input_path = "img1.jpg"   
img = Image.open(input_path)

img_np = np.array(img)
print("Matris boyutu:", img_np.shape)     # (H,W,3) veya (H,W)

dpi = img.info.get("dpi", None)
jfif_density = img.info.get("jfif_density", None)
print("dpi:", dpi, "| jfif_density:", jfif_density)

plt.figure()
plt.imshow(img_np)
plt.title("Orijinal Görüntü")
plt.axis("off")
plt.show()



#-----------------------------------------------------------------------------

#MATRİS HAZIRLIĞI: İstenen dönüşümler

sx, sy = 1.2, 1.2   # %20 büyütme
kx, ky = 0.2, 0.0   # x yönünde kayma
theta = np.deg2rad(30)  # 30 derece
tx, ty = 50, 50 # öteleme


c, s = np.cos(theta), np.sin(theta)

S = np.array([[sx, 0,  0],
              [0,  sy, 0],
              [0,  0,  1]], dtype=float)

Sh = np.array([[1,  kx, 0],
               [ky, 1,  0],
               [0,  0,  1]], dtype=float)

R = np.array([[c, -s, 0],
              [s,  c, 0],
              [0,  0, 1]], dtype=float)

T = np.array([[1, 0, tx],
              [0, 1, ty],
              [0, 0, 1]], dtype=float)

M = T @ R @ Sh @ S
print("Affin matris M:\n", M)


#-----------------------------------------------------------------------------

# SINIR HESAPLAMA: köşeleri dönüştür

w, h = img.size

corners = np.array([
    [0,  w, 0,  w],
    [0,  0, h,  h],
    [1,  1, 1,  1]
], dtype=float)

new_corners = M @ corners
xs = new_corners[0, :]
ys = new_corners[1, :]

min_x, max_x = float(xs.min()), float(xs.max())
min_y, max_y = float(ys.min()), float(ys.max())

new_w = int(np.ceil(max_x - min_x))
new_h = int(np.ceil(max_y - min_y))
new_w, new_h = max(1, new_w), max(1, new_h)

print("Yeni boyut (W,H):", (new_w, new_h))

# negatif koordinatları sıfıra çekmek için düzeltme matrisi
C = np.array([[1, 0, -min_x],
              [0, 1, -min_y],
              [0, 0,  1]], dtype=float)

M2 = C @ M


#-----------------------------------------------------------------------------


Minv = np.linalg.inv(M2)

# PIL AFFINE param: input_x = a*x + b*y + c, input_y = d*x + e*y + f
a, b, c_ = Minv[0,0], Minv[0,1], Minv[0,2]
d, e, f_ = Minv[1,0], Minv[1,1], Minv[1,2]
data = (a, b, c_, d, e, f_)

out_img = img.transform(
    (new_w, new_h),
    Image.AFFINE,
    data,
    resample=Image.BILINEAR
)

output_path = "augmented_img1.png"
out_img.save(output_path)
print("Kaydedildi:", output_path)

plt.figure()
plt.imshow(np.array(out_img))
plt.title("Augmented (Scale+Shear+Rotate+Translate) - Bilinear")
plt.axis("off")
plt.show()


#-----------------------------------------------------------------------------








