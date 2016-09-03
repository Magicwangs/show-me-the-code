# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 16:14:37 2016

@author: MagicWang
"""

from cv2 import *

img=imread('7.jpg',1)
#putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
#lineType=LINE_AA表示16
#bottomLeftOrigin:When true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.
putText(img,text='7',org=(600,100),fontFace=FONT_HERSHEY_SIMPLEX,
        fontScale=3,color=(0,0,255),thickness=8,lineType=16,bottomLeftOrigin=False)
imshow('image',img)
k = waitKey(0)