#Segment cells from image

import cv2
import numpy as np
from matplotlib import pyplot as plt

def segment_cells():
    # Load the image
    input = cv2.imread("resources/cells/1.TIF")

    # Filter only green cells
    img = input[:,:,1]

    thresh , img_bin = cv2.threshold(img, 0, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # min max
    square_shape = np.ones((4,4), np.uint8)
    img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, square_shape, iterations=2)

    # sure background area
    sure_bg = cv2.dilate(img_bin, square_shape, iterations=3)
    
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(img_bin, cv2.DIST_L2, 5)
    cv2.normalize(dist_transform, dist_transform, 0, 1.0, cv2.NORM_MINMAX)
    
    ret, sure_fg = cv2.threshold(dist_transform, 0.90 * dist_transform.max(), 255, 0)
    
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1
    markers *= 100
    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0

    img_jet_colormap = cv2.applyColorMap(np.uint8(markers), cv2.COLORMAP_JET)
    
    cv2.imshow("bg", sure_bg)
    cv2.imshow("fg", sure_fg)
    cv2.imshow("distance", dist_transform)
    cv2.imshow("JET colormap", img_jet_colormap)
    cv2.waitKey()
    cv2.destroyAllWindows()

    watershed_markers = cv2.watershed(input, markers)
    output = input.copy()
    output[watershed_markers == -1] = [255,0,0]

    cv2.imshow("after watershed", output)
    cv2.waitKey()
    cv2.destroyAllWindows()

def main():
    segment_cells()

if __name__ == "__main__":
    main()
