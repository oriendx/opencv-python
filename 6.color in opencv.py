#Colour
#opencv's colour space
#hsv, hsl, yuv, etc.

#hsv.
#h hue
#s saturation (controls the amount of white blended in, the higher the value, the less white)
#v brightness (controls the amount of black blended in, the higher the value, the less black)

#hsl.
#s saturation (not the same as hsb, not related to black and white, but more akin to dilution/concentration)
#l luminance (controls the amount of black and white blended in)

#yuv.
#colour encoding formatfor videos, use little bandwidth, used in TV programmes
#y luminance, also known as grey scale value
#uv chroma
#sampling rate 4:4:4 fully sampled
#See int309 and int302 for details

#check the number of different colours in a picture
import cv2
from pandas import DataFrame

tiger = cv2.imread('E:\\matkasur.jpg')

#Create DataFrame with each pixel
#combine the first two colour dimensions of the image, leaving the third untouched
df = DataFrame(tiger.reshape(-1,3))
#df.head()
#dataframe elements from the first line to see if there are duplicates and add up the resulting boolean values
#df.duplicated().sum()
# view the total number of elements
#df.shape
print(df.shape, df.duplicated().sum())



#Color space transformation
#key api cv2.cvtColor
import cv2

def callback(value):
    pass

cv2.namedWindow('color', cv2.WINDOW_NORMAL)
cv2.resizeWindow('color', 640, 480)

tiger = cv2.imread('E:\\matkasur.jpg')

# Define a list of colour space transformations
colorspace = [
    #All transformation functions start with COLOR
    #In jupyter, press and hold the table key to see the functions in the directory
    cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2YUV,
    cv2.COLOR_BGR2HSV
cv2.createTrack]

cv2.createTrackbar('trackbar', 'color', 0, 2, callback)

while True:
    # Get the trackbar value
    index = cv2.getTrackbarPos('trackbar', 'color')
    
    #Conduct a colour space conversion
    #cv2.COLOR_BGR2RGB These things actually print out as numbers
    cvt_img = cv2.cvtColor(tiger, colorspace[index])
    cv2.imshow('color', cvt_img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
        
cv2.destroyAllWindows() 

