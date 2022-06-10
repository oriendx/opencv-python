What is opencv
OpenCV is a computer vision library developed by Intel. It consists of a set of C and C++ functions.
It implements many common algorithms for image processing and computer vision.
comparing to matlab, it is open source, cross-platform and faster
Note that matlab provides an interface for opencv
https://ww2.mathworks.cn/matlabcentral/fileexchange/47953-computer-vision-toolbox-interface-for-opencv-in-matlab

Environment configuration (pycharm)
opencv provides a native version of c++ and a supported version of python, see this article
https://blog.csdn.net/zhuwei0710/article/details/69802995
to see the differences

Create a new computer vision virtual environment
conda create -n env-name python=xx
where name is the environment name and xx refers to the python version. To use a specific version of opencv, python 3.6 should be installed


## Package Plan ##
environment location: E:\anaconda\envs\env-opencv_study

done
#done
# To activate this environment, use
#
# $ conda activate env-opencv_study
# done
# To deactivate an active environment, use
#
# $ conda deactivate


At this point you can also view the newly created virtual environment with conda info -e

To remove a virtual environment
conda remove -n env-name --all
Remove a package
conda remove --name env-name package-name

Install the virtual environment package
E:\anaconda\envs\env-opencv_study>pip install virtualenv
Name the environment
E:\anaconda\envs\env-opencv_study>virtualenv venv
created virtual environment CPython3.8.5.final.0-64 in 4575ms

Enter the virtual environment
E:\anaconda\envs\env-opencv_study\Scripts>activate
(base) E:\anaconda\envs\env-opencv_study\Scripts>

Installing opencv
It is best to install version 3.4.1.15, as some algorithms have been patented in later versions and are no longer available
(base) E:\anaconda\envs\env-opencv_study\Scripts>pip install opencv-python==3.4.1.15

If you install a version of python other than 3.6, you will get an error when you enter the install command, because that version has been removed from this installation method
ERROR: Could not find a version that satisfies the requirement opencv-python==3.4.1.15
You should delete the environment or the python installation and start again

Since my anaconda installation is on the e drive, this time it says
 WARNING: The script f2py.exe is installed in 'E:\anaconda\envs\env-opencv_study\Scripts' which is not on PATH.
  Consider adding this directory to PATH

Enter the system environment variables
win+r, sysdm.cpl Go to System Properties, select Advanced, Set Environment Variables
Add E:\anaconda\envs\env-opencv_study\Scripts to the PATH

Install other dependency packages
opencv-contrib-python==3.4.1.15 #This is the extension package for opencv
jupyter 
matplotlib 
numpy 
pandas
If you are in China, you should use a domestic mirror, such as douban https://pypi.doubanio.com/simple/

When finished, check if you can import cv2, if you can, the installation is successful
(base) E:\anaconda\envs\env-opencv_study\Scripts>ipython
In [1]: import cv2

View version
In [3]: cv2.__version__
Out[3]: '3.4.1'

The environment is set up successfully, exit with exit()
test if jupyter is usable:

#(base) E:\anaconda\envs\env-opencv_study\jupyter notebook Call up jupyter with scripts as the root directory
#(base) E:\anaconda\envs\env-opencv_study\Scripts> cd . /...
#New folder and notebook
#import the opencv package, the command opencv is called cv2
import cv2
#error,  presumably because jupyter is calling the default Python interpreter
#Solution
#Install the plugin nb_conda to allow self-selection of virtual environments
#E:\anaconda>conda install nb_conda
#This will allow the selecting of opencv environments 

#Create a window
#cv2.nameWindow('window',cv2.WINDOW_AUTOSIZE)
#cv2.WINDOW_AUTOSIZE does not allow modification of the window size
cv2.namedWindow('window',cv2.WINDOW_NORMAL)
#Change the size of the outgoing window
cv2.resizeWindow('window',600,800)
#Show the window with the name windwo
cv2.imshow('window',0)
#Window won't load, switch to pycharm(f**k)

#Set up the interpreter
#Pycharm "Files "settings "Project Interpreter "ana existing enviorment "conda\envs\env-opencv_study\python.exe
