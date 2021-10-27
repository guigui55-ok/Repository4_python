"""フォーム上に画像を表示する"""
import cv2
bgr = cv2.imread('tori3.png')
cv2.imshow("", bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()