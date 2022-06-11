# Control the mouse
# Record mouse coordinates, events, etc.
import cv2
import numpy as np

# The function name can be arbitrary, but the parameters must be five
#These are the mouse event event, the coordinates x,y, the key combination flags, the user data userdata
#The exact correspondence can be found in
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)
    
cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)
#Length and width, just the opposite of row
cv2.resizeWindow('mouse', 640, 360)

#set mouse callback function
cv2.setMouseCallback('mouse', mouse_callback, '123')

#Generate all-black image
#Generate a multi-dimensional array of ndarray with all 0 elements
#numpy.zeros(shape, dtype=float, order='C')
#shape = (row, column, number of elements)
#a=np.zeros((6, 2))=array([[0., 0.], [0., 0.], [0., 0.], [0., 0.], [0., 0.], [0., 0.], [0., 0.]])
img = np.zeros((360, 640 ,3))

while True:
    cv2.imshow('mouse', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()


#TrackBar control
#Control the value of the element (here in rgb) to generate
import cv2
import numpy as np

cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)
cv2.resizeWindow('trackbar', 640, 480)

def callback(value):
    #print(value)
    pass

cv2.createTrackbar('R', 'trackbar', 0, 255, callback)
cv2.createTrackbar('G', 'trackbar', 0, 255, callback)
cv2.createTrackbar('B', 'trackbar', 0, 255, callback)

# background image
img = np.zeros((480, 640, 3), np.uint8)

while True:
    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')
    
    #Modify the image colour with the three values obtained
    #opencv is sorted by bgr
    img[:] = [b, g, r]
    cv2.imshow('trackbar', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
