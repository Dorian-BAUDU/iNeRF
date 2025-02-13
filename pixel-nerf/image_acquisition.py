import os
import time

from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow, destroyAllWindows

os.environ['OPENCV_LOG_LEVEL'] = 'OFF'
os.environ['OPENCV_FFMPEG_LOGLEVEL'] = "-8"
os.environ['QT_DEBUG_PLUGINS'] = '0'
os.environ['QT_NO_DEBUG_OUTPUT']='1'
os.environ['QT_NO_INFO_OUTPUT'] = '0'

def port_selection():
    port_index = None
    for index in range (10):
        try:
            cam=VideoCapture(index)
            if cam.isOpened():
                print(f"Camera port {index} is open.")
                port_index = index
        except:
            print("[INFO] Cam port unaccessible ...")
    
    if port_index == None:
        print("[INFO] No port with camera accessible.")
    else:
        print(f"Camera port is {port_index}.")
    return port_index

def capture_image():
    cam_port = port_selection()
    cam = VideoCapture(cam_port)

    if not cam.isOpened():
        print("[ERROR] Cannot open camera")
        exit()

    print("_______Starting_Image_Capture_______")


    result, image = cam.read()

    while True:
        imshow("image", image)
        if waitKey(1) & 0xFF == ord('y'):
            imwrite(f"image_{time.time()}.png", image)
            destroyAllWindows()
            break

    cam.release()

    return image

def capture_video_stream():
    cam_port = port_selection()
    cam = VideoCapture(cam_port)

    if not cam.isOpened():
        print("[ERROR] Cannot open camera")
        exit()

    print("_______Starting_Video_Stream_______")

    while True:
        result, image = cam.read()
        if result:
            imshow("camera video", image)
            imwrite(f"cam_image_{time.time()}.png", image)
        else:
            print("[ERROR] Can't reach the camera.")
        if waitKey(1)==ord('q'):
            break
        time.sleep(0.01)

    cam.release()
    destroyWindow("camera video")

def capture_video_stream_frame():
    cam_port = port_selection()
    cam = VideoCapture(cam_port)
    image = None

    if not cam.isOpened():
        print("[ERROR] Cannot open camera")
        exit()

    print("_______Starting_Video_Stream_______")
    print("Press 'y' to capture the frame.")

    while True:
        result, frame = cam.read()
        if result:
            imshow("camera video", frame)
        else:
            print("[ERROR] Can't reach the camera.")
        if waitKey(1)==ord('q'):
            break
        if waitKey(1)==ord('y'):
            print("[INFO] Saving frame ...")
            image = frame
            imwrite(f"cam_image_{time.time()}.png", frame)
            break

    cam.release()
    destroyWindow("camera video")

    return image

if __name__ == '__main__':
    print("---[START]---")
