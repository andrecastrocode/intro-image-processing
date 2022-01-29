#Extract image features (Edge detection, corner detection...)

import cv2
import numpy as np
from matplotlib import pyplot as plt

def demo_edge():
    img = cv2.imread("resources/sudoku.jpg")

    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(20, 20))
    plt.subplot(2, 2, 1)
    plt.title("Original")
    plt.imshow(image)
    # Grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # Canny edges
    edged = cv2.Canny(gray, 100, 170, apertureSize = 3)
    plt.subplot(2, 2, 2)
    plt.title("Canny Edges")
    plt.imshow(edged)
    # Finding Contours
    contour, hier = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    plt.subplot(2, 2, 3)
    plt.imshow(edged)
    #print("Count of Contours  = " + str(len(contour)))
    # All contours
    cv2.drawContours(image, contour, -1, (0,255,0), 1)
    plt.subplot(2, 2, 4)
    plt.title("Contours")
    plt.imshow(image)
    
    plt.waitforbuttonpress()
    plt.close('all')

def demo_corner():
    img = cv2.imread("resources/chess.jpg")

    # Grayscaling
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # find Harris corners
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    dst = cv2.dilate(dst,None)
    ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
    dst = np.uint8(dst)
    

    # find centroids
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

    # define the criteria to stop and refine the corners
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

    # Now draw them
    res = np.hstack((centroids,corners))
    res = np.int0(res)
    img[res[:,1],res[:,0]]=[0,0,255]
    img[res[:,3],res[:,2]] = [0,255,0]

    cv2.imshow("corners", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def demo_lines():
    # Load the image
    img = cv2.imread("resources/sudoku.jpg")
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(20, 20))

    # Grayscale 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Canny Edges
    edges = cv2.Canny(gray, 100, 170, apertureSize = 3)
    plt.subplot(1, 2, 1)
    plt.title("edges")
    plt.imshow(edges)

    # Run HoughLines Fucntion 
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

    # Run for loop through each line
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x_1 = int(x0 + 1000 * (-b))
        y_1 = int(y0 + 1000 * (a))
        x_2 = int(x0 - 1000 * (-b))
        y_2 = int(y0 - 1000 * (a))
        cv2.line(image, (x_1, y_1), (x_2, y_2), (255, 0, 0), 2)
    # Show Final output
    plt.subplot(1, 2, 2)
    plt.imshow(image)

    plt.waitforbuttonpress()
    plt.close('all')


def main():
    demo_edge()
    demo_lines()
    demo_corner()


if __name__ == "__main__":
    main()