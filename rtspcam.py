import cv2
import time
import os
from apicam import Detector

def reset_attempts():
    return 10

def reconnect_camera(attempts):
    while True:
        cam = cv2.VideoCapture("")

        if cam.isOpened():
            print("[INFO] Camera connected at " + time.strftime("%Y-%m-%d %H:%M:%S"))
            attempts = reset_attempts()
            return cam, attempts
        else:
            print("Camera not opened " + time.strftime("%Y-%m-%d %H:%M:%S"))
            cam.release()
            attempts -= 1
            print("attempts: " + str(attempts))

            # give the camera some time to recover
            time.sleep(5)

            if attempts <= 0:
                print("Maximum attempts reached. Exiting.")
                exit()

# Set countdown timer
timer = 20
retry_count = 0
max_retries = 3

while True:
    cam, retry_count = reconnect_camera(retry_count)

    while cam.isOpened():
        check, frame = cam.read()

        if not check:
            print("Error: Unable to capture frame from camera. Retrying...")
            cam.release()
            cam, retry_count = reconnect_camera(retry_count)
            continue

        prev = time.time()
    
        while timer >= 0:
            check, frame = cam.read()

            if not check:
                print("Error: Unable to capture frame from camera. Retrying...")
                cam.release()
                cam, retry_count = reconnect_camera(retry_count)
                continue

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
            if cur - prev >= 1:
                # Print current timer
                print(timer) 
                prev = cur 
                timer -= 1
        
                if timer == 0:
                    # Save the frame 
                    file_path = os.path.join('uploads', 'camera.jpg')
                    if frame is not None:
                        cv2.imwrite(file_path, frame) 
                        print("=== Photo taken! ===")

                        # Initialize detector
                        detector = Detector(model_name='rapid',
                                            weights_path='./weights/pL1_MWHB1024_Mar11_4000.ckpt',
                                            use_cuda=False)
                        # Perform object detection
                        detector.detect_one(img_path=file_path,
                                            input_size=1024, conf_thres=0.3,
                                            visualize=True)
                    else:
                        print("Error: Empty frame received from camera")

                    # Reset the timer for the next capture
                    timer = 20
           
    cv2.destroyAllWindows()  # Close OpenCV windows

