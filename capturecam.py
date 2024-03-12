import cv2
import time
import os
from apicam import Detector
import numpy as np

# Set countdown timer
timer = int(20)

source = "rtsp://user:test1234@192.168.1.101:8554/profile0"
cam = cv2.VideoCapture(source)

while True:
    check, frame = cam.read()

    prev = time.time()
  
    while timer >= 0:

        check, frame = cam.read()

        # Display Camera on each frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str("Camera"),
                    (200, 250), font, 
                    3, (0, 0, 255), 
                    2, cv2.LINE_AA) 

        # current time 
        cur = time.time()

        # Update and keep track of Countdown 
        # if time elapsed is one second  
        # then decrease the counter 
        if cur-prev >= 1:
            #Print current timer
            print(timer) 
            prev = cur 
            timer -= 1

    else:
        # Save the frame 
        file_path = os.path.join('uploads', 'camera.jpg')
        cv2.imwrite(file_path, frame) 

        print("=== Photo taken! ===")
        timer = 20
        
        # Initialize detector
        detector = Detector(model_name='rapid',
                   weights_path='./weights/pL1_MWHB1024_Mar11_4000.ckpt',
                   use_cuda=False)

	# A simple example to run on a single image and plt.imshow() it
        detector.detect_one(img_path='./uploads/camera.jpg',
                            input_size=1024, conf_thres=0.3,
                            visualize=True)
		
   # Wait for a short delay (10 milliseconds) to ensure the frame updates
    if cv2.waitKey(20) == ord("q"):
       print("Exiting..")
       break
       
cam.release()
cv2.destroyAllWindows()

