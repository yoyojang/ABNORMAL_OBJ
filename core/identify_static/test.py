import cv2
import time

file = r'D:\Development\ABNORMAL_OBJ\data\video_in\10.20.103.184_03_20200416101236298.mp4'

video = cv2.VideoCapture(file)
fps = video.get(cv2.CAP_PROP_FPS)
print('视频帧率：{}'.format(fps))

n = 0
start = time.time()
while video.isOpened():
    n += 1
    ret, frame = video.read()
    if ret and cv2.waitKey(1) & 0xff != ord('q'):
        frame = cv2.resize(frame,dsize=None,fx=0.5,fy=0.5)
        cv2.imshow('frame', frame)
    else:
        break
    if n%fps == 0:
        end = time.time()
        print('间隔时间：{}'.format(end-start-n/fps+1))

cv2.destroyAllWindows()
video.release()
