import cv2
from flask import Flask, Response

app = Flask(__name__)

# Use a video file or camera as the video source
# For a video file, replace 'video.mp4' with your file path
# For a camera, use the camera index (0 for the default camera)
video_source = './camoflage.mp4'  # or 0 for the default camera

def generate_frames():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            print("all frames read")
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            if ret:
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                
@app.route('/')
def index():
    return "Welcome to the IP Camera Simulation!"

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
