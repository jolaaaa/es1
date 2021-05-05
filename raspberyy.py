import cv2

 webcam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
 face_cascade= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
 profile_cascade= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface_default.xml")t0=time.time()
 
def rett(detected, image, color, flip=False):
    img=image.shape[] for x, y, width, height in detected:
    if flip:
        cv2.rectangle(image, (img-width-x, y), (img-x, y+height), color, thickness= 2)
    else:
        cv2.rectangle(image, (x, y), (x + width, y + height), color, thickness= 2)
            
while True:
    _, frame= webcam.read()
    frame= cv2.flip(frame, 1)

    img_gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(image=img_gray, scaleFactor=1.06, minNeighbors=6)
    profiles_destra = profile_cascade.detectMultiScale(image=img_gray, scaleFactor=1.1, minNeighbors=6)
    img_gray=cv2.flip(img_gray, 1)
    profiles_sin = profile_cascade.detectMultiScale(image=img_gray, scaleFactor=1.1, minNeighbors=6)
    img=cv2.imenCode(".jpg", frame)[1].tobytes() 
    
    rett(faces, frame(0, 255, 0))
    rett(profiles_destra, frame(0, 0, 255))
    rett(profiles_sin, frame(255, 0, 0), True)
    cv2.imshow("Cam", frame)
    
def send_pic(bot, frame):
    _, frame= cv2.imenCode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
    bot.send_photo(chat_id=361881582, photo=frame.tobytes())