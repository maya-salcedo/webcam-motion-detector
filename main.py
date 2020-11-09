import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # will create a face cascadeclassifier

img = cv2.imread("lecture/news.jpg") # to load image into python

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # to create a variable that make the img also in grayscale
                                                # it converts the color img to gray

#get the pixels of the face; the location and height and width of the rectangle where face is located
#scaleFactor=1.05 --> python will find the image by 5%; bigger value like 1.5 will be less accurate but faster than small valu
# minNeighbors --> tell python how many neighbors to search around windows; experiment what number give better results
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

for x, y, w, h in faces: #to get face in the rectangle area
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0, 255, 0), 3) #(0:blue, 255:green, 0:red), 3:width of rectangle
print(type(faces))
print(faces)

#.shape[1] is width of the image, .shape[0] is the height of the omage
#convert to int because you might get a float
resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3,)))

cv2.imshow("Gray", resized) # to show the image
cv2.waitKey(0)
cv2.destroyAllWindows()

