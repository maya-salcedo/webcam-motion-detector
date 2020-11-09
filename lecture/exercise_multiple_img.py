import cv2
import glob

images = glob.glob("lecture/pictures/*.jpg") # this will create a list of the path of the file

for image in images:
    img = cv2.imread(image, 0)
    resized = cv2.resize(img,(100,100))
    cv2.imshow("Hey", resized)
    cv2.waitKey(500) #500 milliseconds
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, resized)

#if the is an empty folder named "resized_pictures" and the pictures are saved in a folder
# that has same level, resized files will be saved in that location

#if there is no folder, the file will have the filename resized_imagename and will be
#saved on the same level

#if there the pictures are saved in a folder but there no output folder or if there is and its name
#is totally not related to pictures, the resized file will be saved something I can locate