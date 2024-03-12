import cv2
import time
import os

# Set countdown timer
timer = int(5)

source = ----
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
        file_path = os.path.join(save_folder, 'camera.jpg')
        cv2.imwrite(file_path, frame) 

        print("=== Photo taken! ===")
        timer = 5

    # Wait for a short delay (10 milliseconds) to ensure the frame updates
    if cv2.waitKey(10) == ord("q"):
       break


cam.release()
cv2.destroyAllWindows()
