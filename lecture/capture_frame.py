import cv2, time

video = cv2.VideoCapture(0)
#if you have a video file, put the file path as parameter
#if want to use the built in webcam, 0 may be used
#if you have 2nd camera, 1 may be used
#if there is 3rd camera, 2 may be used
check, frame = video.read()
#check: boolean

print(check)
print(frame)

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #to conver the colored frame to gray
time.sleep(3) #to let python wait for 3 seconds
cv2.imshow("Capturing", gray)


cv2.waitKey(0) #it is needed when you use .imshow
video.release() #to access the object in the video
cv2.destroyAllWindows()