#image scaling

import cv2

def scaling_demo():
    img = cv2.imread("resources/bmw_ix.jpg")

    cv2.imshow("original", img)
    cv2.waitKey()

    img = cv2.resize (img, (0,0), fx=0.5, fy=0.5)

    cv2.imshow("half res", img)
    cv2.waitKey()

    img = cv2.resize (img, (0,0), fx=0.5, fy=0.5)

    cv2.imshow("quarter res", img)
    cv2.waitKey()

    cv2.destroyAllWindows()

def rotation_demo():
    img = cv2.imread("resources/bmw_ix.jpg")
    height, width = img.shape[0:2]
    
    cv2.imshow("original", img)
    cv2.waitKey()

    angle = 90
    scale = .5
    rotationMatrix = cv2.getRotationMatrix2D((height/2, width/2), angle, scale)
    rotatedImage = cv2.warpAffine(img, rotationMatrix, (int(height/2), int(width/2)))
    cv2.imshow('Rotated Image', rotatedImage)
    cv2.waitKey()
    cv2.destroyAllWindows()


def crop_demo():
    img = cv2.imread("resources/bmw_ix.jpg")
    height, width = img.shape[0:2]

    cv2.imshow("original", img)
    cv2.waitKey()

    startRow = int(height*.5)
    startCol = int(width*.5)
    endRow = int(height*.95)
    endCol = int(width*.95)
    croppedImage = img[startRow:endRow, startCol:endCol]
    cv2.imshow('Cropped Image', croppedImage)
    cv2.waitKey()
    cv2.destroyAllWindows()

def blur_demo():
    img = cv2.imread("resources/bmw_ix.jpg")
    
    cv2.imshow("original", img)
    cv2.waitKey()
    
    blur_image = cv2.GaussianBlur(img, (7,7), 0)
    cv2.imshow('Gaussian Blur Image', blur_image)
    cv2.waitKey()

    blur_image = cv2.medianBlur(img,5)
    cv2.imshow('Median Blur Image', blur_image)
    cv2.waitKey()

def main():
    scaling_demo()
    rotation_demo()
    crop_demo()
    blur_demo()

if __name__ == "__main__":
    main()
