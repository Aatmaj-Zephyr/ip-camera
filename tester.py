import time
import cv2

# Replace 'YOUR_IP_CAMERA_URL' with the URL of your IP camera
ip_camera_url = 'http://127.0.0.1:5100/video_feed'

# Create a VideoCapture object to capture frames from the IP camera
cap = cv2.VideoCapture(ip_camera_url)

while True:
    # Read a frame from the IP camera
    ret, frame = cap.read()

    if not ret:
        print("Failed to retrieve frame from the IP camera.")
        break

    # Display the frame in a window
    cv2.imshow('IP Camera Feed', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #time.sleep(10/30)# wait frame time

# Release the VideoCapture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
