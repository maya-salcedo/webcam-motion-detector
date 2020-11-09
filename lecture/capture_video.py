import cv2, time

video = cv2.VideoCapture(0)
#if you have a video file, put the file path as parameter
#if want to use the built in webcam, 0 may be used
#if you have 2nd camera, 1 may be used
#if there is 3rd camera, 2 may be used

a=0 #to get the number of frame created(code:1 of 3)

while True:
    a = a + 1 #to get the number of frame created(code:2 of 3)
    check, frame = video.read() #check: boolean

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #to conver the colored frame to gray
    cv2.imshow("Capturing", gray)
    key = cv2.waitKey(1)

    if key == ord("q"): # to break the while loop, press q
        break

print(a)#to get the number of frame created(code:3 of 3), outside the loop

video.release() #to access the object in the video
cv2.destroyAllWindows()