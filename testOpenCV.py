# -*- coding: utf-8 -*-
"""
Created on Sat May  6 12:18:47 2017

@author: Pedro

Instalar OpenCV con Conda....es compatible con python3.5
conda install -c https://conda.binstar.org/menpo opencv3

Si tienes  python 3.6
conda install python=3.5
conda install -c https://conda.binstar.org/menpo opencv3

Mas...
http://stackoverflow.com/questions/38787748/installing-opencv-3-1-with-anaconda-python3
"""

import cv2 # import the opencv library

 # this will print the version of your opencv2
print(cv2.__version__)