# Data structures: mat

#opencv is using the mat structure to represent structures
#mat is a C++ class
#mat contains both header and data parts
#Here is a partial example of the structure
"""""
class CV_EXPORTS Mat{
    ...
    int dims;//the number of dimensions
    int rows,cols;//number of rows and columns
    uchar *data;//pointer to the data stored
    int *refcount;//reference count
    ...
};
"""""
Properties of #mat
#dims dimension
#rows number of rows, cols number of columns
#depth the bit depth of the pixel
#channels Number of channels, e.g. rgb is 3
#size The size of the matrix
#type dep+dt+chs CV_8UC3 
#depth+data type+channels cv means opencv, 8 means 8 bits, u means unsigned, c3 means 3 channels
#data store the data

#python converts mat to ndarray, which makes some attributes inaccessible
tiger = cv2.imread('E:\\matkasur.jpg')
type.tiger
# return numpy.ndarray
tiger.channels
#returns an error because it has been converted to an ndarray and there is no channel information in it
#Some properties of an ndarray
#data (address of memory, not directly accessible)
#size (number of elements)
#datatype (dtype data type)
#shape (number of rows and columns)
#ndim number of channels/dimensions



#Basic operations: deep and shallow copies
#Basic operations: deep and shallow copies
#deepcopy: assigning the contents of a referenced data type to another variable for storage is called a deep copy
#Shallow copy: assigning the address of a referenced data type to another variable store is called a shallow copy
import numpy as np
import cv2

tiger = cv2.imread('E:\\matkasur.jpg')

# shallow copy
tiger2 = tiger.view()

#deep copy
tiger3 = tiger.copy()

#change tiger's corresponding matrix, with rows corresponding to 10-100, to red (bgr)
tiger[10:100, 10:100] = [0, 0, 255]

cv2.namedWindow('tiger', cv2.WINDOW_NORMAL)
cv2.resizeWindow('tiger', 640, 480)
#Stacking the three images with hstack
#tiger2 is also changed after tiger is modified, as tiger2 only gets the index address and not the data itself
#tiger3 is unaffected as it is a new variable that has acquired data
cv2.imshow('tiger', np.hstack((tiger, tiger2, tiger3)))
cv2.waitKey(0)
cv2.destroyAllWindows()



# Basic operations: image, channel segmentation and fusion
import cv2
import numpy as np

img1 = np.zeros((480, 640 ,3), np.uint8)

# split channels
b, g, r = cv2.split(img1)
#Modify some colours
b[10:100, 10:100] = 255
g[10:100, 10:100] = 100
#Merge to see
img2 = cv2.merge((b, g, r))
cv2.imshow('img', np.hstack((img1, img2)))
cv2.imshow('channels', np.hstack((b, g))))
cv2.waitKey(0)
cv2.destroyAllWindows()


