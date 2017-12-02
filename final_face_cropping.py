import os
import cv2
folder = 'test'
os.mkdir(folder)

# use opencv to do the job
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


print(cv2.__version__)  # my version is 3.1.0
vidcap = cv2.VideoCapture("output1.mp4")
count = 0
while True:
    success,image = vidcap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        ---cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        gray = gray[y: y + h, x: x + w]  # Crop from x, y, w, h -> 100, 200, 300, 400

        try:
            out = cv2.resize(gray, (350, 350))  # Resize face so all images have same size
            cv2.imwrite(os.path.join(folder, "frame{:d}.jpg".format(count)), out)  # save frame as JPEG file
        except:
            pass
        count += 1
print("{} images are extacted in {}.".format(count,folder))
