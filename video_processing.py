import cv2

cascade_path='haarcascade_fullbody.xml'
classfier=cv2.CascadeClassifier(cascade_path)
path=r'C:\Users\chand\Desktop\bgmi1.mp4' #0 for webcam , path to video file
video=cv2.VideoCapture(path)

while True:
    status,image=video.read()
    if not status:
        print('could not read frame')
        break
    #logic
    image=cv2.resize(image,(0,0),fx=0.4,fy=0.4)
    detection=classfier.detectMultiScale(image)
                                          
    if len(detection)>0:
        print(f'Found {len(detection)} people')
        for(x, y, w, h) in detection:
            cv2.rectangle(image,(x,y), (x+w,y+h), (0,255,0),2)
    cv2.imshow('video',image)
    if cv2.waitKey(1)==ord('q'):   #if q is pressed then break
        break
video.release()
cv2.destroyAllWindows()