import cv2
import time
import numpy as np

def get_image():
    images = []
    count=1

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,512)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,512)

    start=time.time()
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if((int(time.time()-start)) == 5 and count < 4):
            start+=5
            count+=1
            images.append(frame)
        
        if(count >= 4):
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    return images
