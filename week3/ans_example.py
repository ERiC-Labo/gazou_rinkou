import cv2
import numpy as np

path = '../inputimage' #画像のあるディレクトリのパス
image_name = 'Lenna.jpg' #画像の名前

image = path + '/' + image_name #パス＋名前

#画像読み込み
img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

#画像の形状表示
print(img.shape)

#画像の縦と横のサイズ取得
h,w=img.shape[:2]
if h > 300 or w > 300:
    img = cv2.resize(img, (300,300))
    h,w=img.shape[:2]

#画像表示
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows

#画像にノイズ付加
noise_level1 = 6
noise_level2 = 250
noise_level3 = 10
noise_level4 = 240

spnoise = np.zeros((h,w), dtype=np.uint8)
cv2.randu(spnoise, 0, 255)
res_noise_img1 = img.copy()
res_noise_img1[noise_level2 < spnoise] = 255
res_noise_img1[noise_level1 > spnoise] = 0
res_noise_img2 = img.copy()
res_noise_img2[noise_level4 < spnoise] = 255
res_noise_img2[noise_level3 > spnoise] = 0

#ノイズ画像を保存
cv2.imwrite('../outputimage/Lenna_noise1.jpg', res_noise_img1)
cv2.imwrite('../outputimage/Lenna_noise2.jpg', res_noise_img2)

#メディアンフィルタでノイズ除去
#1枚目
median_img1 = cv2.medianBlur(res_noise_img1, ksize = 3)
cv2.imwrite("../outputimage/median_1.jpg", median_img1)
#2枚目
median_img2 = cv2.medianBlur(res_noise_img2, ksize = 3)
cv2.imwrite("../outputimage/median_2.jpg", median_img2)

#エッジ抽出
laplacian = cv2.Laplacian(img, cv2.CV_8U)
cv2.imwrite("../outputimage/laplacian.jpg", laplacian)

# 連結
image_v1 = cv2.hconcat([img, res_noise_img1, res_noise_img2])
image_v2 = cv2.hconcat([median_img1, median_img2, laplacian])
out_img = cv2.vconcat([image_v1, image_v2])

cv2.imshow('image', out_img)
cv2.imwrite('../outputimage/concat.jpg', out_img)
cv2.waitKey(0)
cv2.destroyAllWindows
