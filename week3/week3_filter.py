#余裕のある人はフィルタ、画像処理手法、ノイズの閾値などを変更して画像を比較してください
import cv2
import numpy as np

path = '' #画像のあるディレクトリのパス
image_name = '' #画像の名前

image = path + '/' + image_name #パス＋名前

#画像読み込み
img = 

#画像の形状表示
print(img.shape)

#画像の縦と横のサイズ取得
h,w=img.shape[:2]
if h > 300 or w > 300:
    img = cv2.resize(img, (300,300))
    h,w=img.shape[:2]

#画像表示

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
#1枚目
#2枚目

#メディアンフィルタでノイズ除去
#1枚目
median_img1 = 
#画像を保存
#2枚目
median_img2 = 
#画像を保存

#エッジ抽出(ラプラシアンフィルタ)
laplacian = 
#画像を保存

# 連結
image_v1 = cv2.hconcat([img, res_noise_img1, res_noise_img2]) #画像を横方向に連結
image_v2 = cv2.hconcat([median_img1, median_img2, laplacian]) #画像を横方向に連結
out_img = cv2.vconcat([image_v1, image_v2]) #画像を縦方向に連結
#連結画像の表示
#連結画像の保存