import cv2

def main():
    try:
        movie_path = r'C:\ZMyFolder\newDoc\0ProgramingAll\image_sample\parts'
        file_name = 'pad_opening.mp4'
        movie_path += '\\' + file_name
        play_movie(movie_path)
    except:
        import traceback
        print(traceback.print_exc())

def play_movie(movie_path):
    try:
        cap = cv2.VideoCapture(movie_path)

        if (cap.isOpened()== False):  
            print("ビデオファイルを開くとエラーが発生しました") 

        while(cap.isOpened()):

            ret, frame = cap.read()
            if ret == True:

                cv2.imshow("Video", frame)
                
                if cv2.waitKey(25) & 0xFF == ord('q'): 
                    break
            
            else:
                break

        cap.release()

        cv2.destroyAllWindows()
    except:
        import traceback
        print(traceback.print_exc())

main()