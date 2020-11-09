import cv2

img = cv2.imread("galaxy.jpg", 0) #if you want to read to the image as it is, pass 1,
                                    # grayscale, 0 which is 1 band
                                    # transparency capabilities, -1

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2))) #the tuple parameter is the new dimension
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image) #method to save the new img
cv2.waitKey(0) # 0: when user click any button, the window will close
                # 2000: 2 seconds
cv2.destroyAllWindows() # method to close the window
