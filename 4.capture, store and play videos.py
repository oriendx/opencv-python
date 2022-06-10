# capture，store and play video

# Turn on the camera
import cv2

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)

# class name is capitalised, function method is lowercase, VideoCapture is a C++ class
capture = cv2.VideoCapture(0)

while True:
#while capture.isOpened();
    #read each frame and return
    #ret is True if the data was read, False if it wasn't
    ret, frame = capture.read()
    
    #Make a determination based on ret
    #If not read, exit
    if not ret:
        break
        
    #Display the data
    cv2.imshow('video' , frame)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
        
# Here the C++ class is called, so release the resources
capture.release()
cv2.destroyAllWindows()



#Open the video
import cv2

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)

video = cv2.VideoCapture('E:/assets/cat.mp4')

while video.isOpened():
    ret , frame = video.read()
    if not ret:
        break
        
    cv2.imshow('video', frame)
    # Here we set the waitKey to 10, which means that the next frame is played every 10 milliseconds, which is accelerated
    #For a 30 frames per second video, 1000/30 milliseconds between each picture
    # If you set waitKey(1000//30), it's basically playing at the original speed, // which means rounding down
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()   



# Record the video
import cv2

cap = cv2.VideoCapture(0)
#Video is encoded in mpeg-4 and stored as an mp4 file
#You can also write it like this
#cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
storevid = cv2.VideoWriter_fourcc(*'mp4v')
#('X','2','6','4') mpeg-4 encoding, store as mp4 file
#('I', '4', '2', '0') YUV encoding, stored as an avi file
#('P', 'I', 'M', 'I') mpeg-1 encoding, stored as an avi file
#('X', 'V', 'I', 'D') mpeg-4 encoding, stored as mp4
#('T', 'H', 'E', 'O') ogg vorbis encoding, stored in ogv format
#('F', 'L', 'V', '1') flash encoding, stored in flv format

#create videowriter
#frame rate is 30fps, resolution is 640*480
vdwriter = cv2.VideoWriter('E:/assets/output.mp4', storevid ,30 ,(640 , 480))

while cap.isOpened():
    ret , frame = cap.read()
    if not ret:
        break
    
    # Write data for each frame
    vdwriter.write(frame)
    #Window will be created automatically
    cv2.imshow('frame',frame)
    
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()

#  to view the video, end the python instance first


