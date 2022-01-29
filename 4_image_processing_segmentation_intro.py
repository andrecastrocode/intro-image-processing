#intro to segmentation (grayscale, bw, thresholding)

import cv2
from cv2 import COLOR_BGR2GRAY
from matplotlib import pyplot as plt

def demo_thresholding():
    img = cv2.imread("resources/bmw_ix.jpg")
    img = cv2.cvtColor(img, COLOR_BGR2GRAY)

    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]
    
    plt.figure()
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.waitforbuttonpress()
    plt.close('all')

    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    blur = cv2.GaussianBlur(img,(15,15),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Otsu Thresholding', 'Gaussian Blur + Otsu Thresholding']
    
    plt.figure()
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.waitforbuttonpress()
    plt.close('all')



def main():
    demo_thresholding()


if __name__ == "__main__":
    main()