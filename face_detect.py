# pip install opencv-python
#harrascase_frontalface_default.xml
import cv2

face_cascade = cv2.CascadeClassifier(                                        # this line say learn the shape of face from thsi file
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

b=cv2.VideoCapture(0)                                                         # camera on karn=e ki permission dena
while True:
    c_rec,d_image=b.read()
    e=cv2.cvtColor(d_image,cv2.COLOR_BGR2GRAY)
    f=face_cascade.detectMultiScale(e,1.3,6)                              # Detect faces in the grayscale image.
# 1.3 = scaleFactor (image ko zoom karke multiple sizes par check karta hai)
# 6 = minNeighbors (kitni baar confirm hone par usko face mana jaayega)
# Output 'f' me sab detected faces ke (x, y, width, height) values store hoti hain
#f = face_cascade.detectMultiScale(e, 1.3, 6)


    # faces=face_cascade.detectMultiScale(e,1.3,5)

    for (x,y,w,h) in f:
        cv2.rectangle(d_image,(x,y),(x+w,y+h),(255,0,0),5)   #Face mil gaya → uske around box bana diya 

    cv2.imshow('img',d_image)                                     #
    h=cv2.waitKey(40) & 0xFF                # waitKey(40) ka matlab hai ki har 40 milliseconds me ek frame capture karo aur usko display karo. Agar user ne 'q' key press kiya to loop se bahar nikal jao.
    if h==40:
        break
b.release()
cv2.destroyAllWindows()   
