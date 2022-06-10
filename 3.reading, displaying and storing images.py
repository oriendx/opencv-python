# Image reading and display
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mping

# Read the image
# The path format is double backslash \\ or single slash /, which can be read directly in the current directory
# Color image without flags
# jpg images are read as uint8 (8-bit binary numbers without plus or minus, numbers 0-255)
tiger = cv2.imread('E:\\matkasur.jpg')
plt.imshow(tiger1)
# The maximum element of the matrixed image is 255
tiger.max()
# The colour of the image shown here has changed because the data read by opencv is not the default RGB channel arrangement
# Instead, it is a BGR arrangement
# Use cv2.imshow() to avoid this
cv2.imshow('tiger', tiger)
key = cv2.waitKey(0)
if key == ord('q'):
    print('Preparing to destroy window')
    cv2.destroyAllWindows()
    
# Now wrap the above code into a function and save it separately
# save it as a py file, because
# jupyter saves the contents of a file in json format, rather than the normal format of a python file.
# so it can't be parsed directly by a python parser
"""""
def cv_show(name, img):
    cv2.imshow(name, img)
    key = cv2.waitKey(0)
    if key == ord('q'):
        cv2.destroyAllWindows()
        
"""""

# Call and try
# successful
from utilities import cv_show
%run utilities.py
cv_show('tiger',tiger)

# Save the image
import cv2
# import os library for easy saving to a specified folder
# The usage can be found at
# https://github.com/python/cpython/blob/3.7/Lib/os.py
# https://zhuanlan.zhihu.com/p/82029511
import os

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 640, 480)

img = cv2.imread('E:\\matkasur.jpg')

while True:
    cv2.imshow('img',img)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break
    elif key == ord('s'):
        path = "C:/Users/24599/Desktop"
        # use os.path.join to stitch paths
        cv2.imwrite(os.path.join(path , 'savetest.jpg'), img)
    else:
        print(key)
        
cv2.destroyAllWindows()

# Now wrap the above
""""
def save_to_desktop(name, img)
    while True:
     cv2.imshow('img',img)
     key = cv2.waitKey(0)
      if key == ord('q'):
        break
      elif key == ord('s'):
        path = "C:/Users/Desktop"
        # use os.path.join to stitch paths
        cv2.imwrite(os.path.join(path , 'savetest.jpg'), img)
       else:
        print(key)
        
     cv2.destroyAllWindows()
"""""

# Call and execute to try
# successful
import cv2
from utilities import save_to_desktop
%run utilities.py
tiger = cv2.imread('E:\\matkasur.jpg')
save_to_desktop('tiger', tiger)
# The various indent errors are caused by indentation errors


