#Segment cells from image

import cv2
import numpy as np
from matplotlib import pyplot as plt

def segment_cells():
    # Load the image
    img = cv2.imread("resources/cells/1.TIF")

    # Filter only green cells
    img = img[:,:,1]

    thresh , img_bin = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # min max
    square_shape = np.ones((4,4),np.uint8)
    img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, square_shape, iterations=2)

    # sure background area
    sure_bg = cv2.dilate(img_bin, square_shape, iterations=3)
    
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(img_bin, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
    
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    cv2.imshow("msg", sure_fg)

    cv2.waitKey()
    cv2.destroyAllWindows()

def main():
    segment_cells()

if __name__ == "__main__":
    main()
