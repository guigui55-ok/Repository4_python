"""フォーム上に画像を表示する"""
import cv2
bgr = cv2.imread('./image/test1/tori3.png')
cv2.imshow("img", bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()