import cv2

# Create a window
# cv2.nameWindow('window',cv2.WINDOW_AUTOSIZE)
# cv2.WINDOW_AUTOSIZE does not allow modifying the window size
cv2.namedWindow('window', cv2.WINDOW_NORMAL)

# Change the size of the window
cv2.resizeWindow('window', 600, 800)

# Show the window with the name window
cv2.imshow('window', 0)

# Add a waitKey of 0 to avoid window flickering
# This function should be written as wait_key according to the python specification, here it is written in c
# Pressing any key will cause wait to end and return the ASCII code for that key
# The function ord('example_key') which calculates ASCII
# 0 means any key press is accepted, other integer values indicate the time in milliseconds that the wait key was pressed
# cv2.waitKey(0)
# Can be used to end a window
key = cv2.waitKey(0)
# Because key is an int type of at least 16 bits and the ASCII code is eight bits, it is sometimes written like this
# if key & 0xFF == ord('q')
# fetch the last eight bits of key (one F is four bits, two F's are eight bits)
# You can leave it out in python, but you must write it this way in C++
if key == ord('q'):
    print('Preparing to destroy window')
    cv2.destroyAllWindows()
# Found pycharm not very suitable for data processing, switch back to jupyter notebook (f**k again)

