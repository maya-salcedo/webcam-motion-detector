import cv2, time, pandas
from datetime import datetime


first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start", "End"]) #will create dataframe structure

video = cv2.VideoCapture(0)
        #if you have a video file, put the file path as parameter
        #if want to use the built in webcam, 0 may be used
        #if you have 2nd camera, 1 may be used
        #if there is 3rd camera, 2 may be used

while True:
    check, frame = video.read() #check: boolean
    status = 0 #to denote that there is no motion in the current frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #to convert the colored frame to gray
    gray = cv2.GaussianBlur(gray, (21,21), 0) # to make image blurry to remove noise and increase accuracy, 2nd param is width and height;
                                                #3rd param is standard deviation, 0 is commonly used
    if first_frame is None:
        first_frame = gray
        continue # so the python will go back to the beginning of loop and not process the code after this line
                # in the following iteration of the loop, first_frame has not any None so it will skip this if loop

    delta_frame = cv2.absdiff(first_frame, gray)

            # we want to assign those with threshhold of 30, a value of 255
            # .threshold produces a tuple, [1] so access the second elementq
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2) #iteration value: bigger value, smoother the image

    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            #find all the contours of the distinct object in this image
            #all the contours will be saved in the cnts variable

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue #tells to go back to the 1st step of the loop
        status = 1 #this code means that python find a motion in the video

        (x, y, w, h) = cv2.boundingRect(contour)#to draw a rectangle if the countour area is > 1000
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
                #x,y is the coordinate of left upper corner of rectangle
                # (x+w, y+h) is the coordinate of the right lower corner of the rectangle
                #(0, 255, 0) color of rectangle
                #3 is the width of the rectangle
    status_list.append(status)

    status_list = status_list[-2:] #to save on memory

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())



    cv2.imshow("Gray Frame", gray) #1st param is name of window
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)
    key = cv2.waitKey(1)

    if key == ord("q"): # to break the while loop, press q
        if status==1:
            times.append(datetime.now())
        break
print(status_list)
print(times)

for i in range(0,len(times), 2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv") #this is the data frame

video.release() #to access the object in the video
cv2.destroyAllWindows()