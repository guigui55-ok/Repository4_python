import cv2

read_path = 'image/power_on_screen.png'
temp_path = 'image/key_mark3.png'
# 画像の読み込み
img = cv2.imread(temp_path, 0)

# 閾値の設定
threshold = 100

# 二値化(閾値100を超えた画素を255にする。)
ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

#オリジナル画像の高さ・幅を取得
# img = img_thresh
# height = img.shape[0]
# width = img.shape[1]
# #リサイズ(拡大/縮小)
# multiple =0.5
# img = cv2.resize(img , (int(width * multiple), int(height * multiple)))

# 二値化画像の表示
cv2.namedWindow("img_th", cv2.WINDOW_NORMAL)
cv2.imshow("img_th", img_thresh)
cv2.waitKey()
cv2.destroyAllWindows()