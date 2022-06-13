#Drawing simple shapes



#Drawing line segments
import cv2
import numpy as np

#Create a solid black background image as a canvas
background = np.zeros((480,640,3), np.uint8)

#cv2.line(img, pt1, pt2, color, thickness, lineType, shift)
#canvas, start point, end point, colour, thickness, line type (the larger the value, the less jagged the line will be, default is 8), zoom ratio
#The following two line segments have a distinctly different jagged feel
line1 = cv2.line(background, (10,20), (300,400), (0,0,255), 5, 4)
line2 = cv2.line(background, (80,100), (380,480), (0,0,255), 5, 16)

cv2.imshow('draw', background)
cv2.waitKey(0)
cv2.destroyAllWindows()



#draw rectangle
import cv2
import numpy as np

#Create a solid black background image as a canvas
background = np.zeros((480,640,3), np.uint8)

#cv2.rectangle(img, pt1, pt2, color, thickness, lineType, shift)
#canvas, start point, end point (two diagonal points to determine a rectangle), colour, thickness, line type (the larger the value, the less jagged the line will be, default is 8), zoom ratio
#The following two rectangles have distinctly different jaggedness at the diagonal points
rect1 = cv2.rectangle(background, (10,20), (300,400), (0,0,255), 5, 4)
rect2 = cv2.rectangle(background, (80,100), (380,480), (0,0,255), 5, 16)

cv2.imshow('draw', background)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Draw a circle
import cv2
import numpy as np

#Create a solid black background image as a canvas
background = np.zeros((480,640,3), np.uint8)

#cv2.circle(img, center, radius, color, thickness, lineType, shift)
#canvas, centre, radius, colour, thickness, line type, zoom ratio
#The two rectangles below have a distinctly different jagged feel at the diagonal points
circle1 = cv2.circle(background, (160,30), 20, (0,0,255), 5, 4)
circle2 = cv2.circle(background, (80,100), 50, (0,0,255), 5, 16)

cv2.imshow('draw', background)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Draw an ellipse
#Can also be used to draw an ellipse
import cv2
import numpy as np

#Create a solid black background image as a canvas
background = np.zeros((480,640,3), np.uint8)

#cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness, lineType, shift)
#canvas, centre of ellipse, axis (i.e. half the length and width, axes for the plural of axis), angle (the amount of rotation, counterclockwise)
# the angle at which the drawing starts, the angle at which it ends (allowing only part of the drawing to be drawn, also in counterclockwise order), the colour, the thickness, the
#line type, scale ratio
#The following two ellipses have different angles and finishes
ellipse1 = cv2.ellipse(background, (320, 240), (100, 50), 0, 0, 360, (0,0,255), 5, 4)
ellipse2 = cv2.ellipse(background, (320, 240), (100, 50), 45, 0, 180, (0,0,255), 5, 4)

cv2.imshow('draw', background)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Draw polygons
import cv2
import numpy as np

#Create a solid black background image as a canvas
background = np.zeros((480,640,3), np.uint8)

#cv2.polylines(img, pts(int32(C++ specified) list or tuple to place individual vertices), isclosed, color, thickness, lineType, shift)
#dataframe with multiple columns should use double brackets, single brackets cause only the first one to be returned
pls = np.array( [[(300, 80), (150, 60), (459, 40)]], np.int32)
polygon = cv2.polylines(background, pls, True, (0,0,255), 5, 4)

#cv2.fillPoly(img, pts, color, thickness, lineType, shift)
#draw a filled (necessarily closed) polygon
cv2.imshow('draw', background)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Draw text
import cv2
import numpy as np

background = np.zeros((480,640,3), np.uint8)
# cv2.putText(canvas, content, position, font cv2.FONT_xxx, font size ,font colour)
cv2.putText(background, 'hello opencv', (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2, [0,0,255])
cv2.imshow('draw', background)
cv2.waitKey(0)
cv2.destroyAllWindows()



# If you want to write Chinese
#need the pillow package (this is actually used for drawing images), which is already pre-installed
#Then import the fonts that come with your computer
#The name PIL is python2 style
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2

#plain white background
#numpy.full(shape, fill_value, dtype=None, order='C')
#returns a new array based on the specified shape and type, filled with fill_value
#shape: integer or sequence of integers
#The shape of the new array, with a single value representing one dimension and a tuple passed as an argument, and the number of elements in the tuple representing the number of dimensions.
#For example, (2, 3) or 2.
#fill_value: scalar (no vector), fills the value of the array
#dtype: data type, optional.
#default is None, see the value of the array to be filled data type: np.array(fill_value).dtype.
#order: {'C', 'F'}, optional, store multidimensional data in row-dominant (C style) or column-dominant (Fortran style) continuous (row or column) order.
img = np.full((200, 200, 3), fill_value = 255, dtype = np.uint8)

#Import the font file
#C:\Windows\Fonts
cnfont = ImageFont.truetype('C:/Windows/Fonts/Deng.ttf')

# Create a pillow of images
img_pil = Image.fromarray(img);

draw = ImageDraw.Draw(img_pil)
# Use draw to draw Chinese
draw.text((100, 150), 'Hello world', font = cnfont, fill = (0, 255, 0, 0))

# revert back to ndarray in order to display it with opencv
img = np.array(img_pil)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


