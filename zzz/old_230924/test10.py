import cv2
#リサイズしたいファイル：input_filepath
input_filepath = r'C:\Users\OK\source\repos\test_media_files\cv2_match_mov_test_media\screenrecord2.mp4'

resize = 2 #ファイルサイズを２分の1にしたい
resize = resize**0.5 #ルート2
print(resize)
cap = cv2.VideoCapture(input_filepath)

#生成する無音動画ファイルのパス
temp_videopath = f".\\temp_video.mp4"

#動画のプロパティを取得
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

#動画をリサイズ
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
min_fps = 30
if fps <= min_fps:
    writer = cv2.VideoWriter(
        temp_videopath,fourcc, 
        fps, (int(width/resize), int(height/resize)))
else:
    writer = cv2.VideoWriter(temp_videopath,fourcc, min_fps, (int(width/resize), int(height/resize)))
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Frame", frame)
    frame = cv2.resize(frame,(int(width/resize), int(height/resize)))
    writer.write(frame)
writer.release()
cap.release()
print("リサイズ完了")

#この後音声を抽出したり結合したりするが割愛