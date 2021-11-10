import cv2
import numpy as np
 
def main():
    try:
        base_path = 'image/power_on_screen.png'
        temp_path = 'image/key_mark2.png'
        temp_path = 'image/key_mark3.png'
        temp_path = 'image/key_mark4.png'
        write_path = 'image/matchtemplate_test5_result.png'
        write_path = 'image/matchtemplate_test5_result'
        
        base_path = 'image/pad07_login.png'
        temp_path = 'image/button_login_ok.png'

        # Input Image
        img  = cv2.imread(base_path,0)
        
        # Template Image
        TempValname = []
        TempFilename = []
        
        TempFilename.append(temp_path)
        max_count = 1
        for i in range(max_count):            
            TempValname.append('Template'+str(i))
        
        for i in range(max_count):
            # Image read
            TempValname[i] = cv2.imread(TempFilename[i],0)
        
        method = cv2.TM_CCOEFF_NORMED

        # Template matching
        for i in range(max_count):
            w, h = TempValname[i].shape[::-1]   # Template image size
        
            res = cv2.matchTemplate(img, TempValname[i], cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            print(str(i) + ' -> max_val: ' + str('{:.3f}'.format(max_val)), ',  max_loc: ' + str(max_loc))
        
            # Result image
            top_left = max_loc
            btm_right = (top_left[0]+w, top_left[1]+h)
            img_temp = img.copy()
            cv2.rectangle(img_temp, top_left, btm_right, 0, 2)
            file_name = write_path + str(i)+'.png'
            cv2.imwrite(file_name,img_temp)
            print(file_name)
    except:
        import traceback
        print(traceback.print_exc())

if __name__ == '__main__':
    main()