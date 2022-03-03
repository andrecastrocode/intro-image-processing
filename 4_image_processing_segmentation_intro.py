#intro to segmentation (grayscale, bw, thresholding)

import cv2
from cv2 import COLOR_BGR2GRAY
from matplotlib import pyplot as plt

def demo_thresholding():
    img = cv2.imread("resources/sudoku.jpg")
    img = cv2.cvtColor(img, COLOR_BGR2GRAY)

    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    hist1 = cv2.calcHist([img],[0],None,[256],[0,256])

    titles = ['Original Image', 'Global Thresholding (v = 127)']
    images = [img, th1, hist1]
    
    plt.figure()
    for i in range(3):
        if i == 2:
            plt.subplot(2,2,i+1),plt.plot(images[i])
            plt.axvline(x=ret, color='r', linestyle='-')
            plt.xlim([0,256])
        else:
            plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])

    plt.waitforbuttonpress()
    plt.close('all')

    otsu1, th5 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    blur = cv2.GaussianBlur(img,(5,5),0)
    hist2 = cv2.calcHist([blur],[0],None,[256],[0,256])
    otsu2,th6 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    titles = ['Otsu Thresholding', 'Otsu Thresholding Histogram', 'Gaussian Blur + Otsu Thresholding', 'Gaussian Blur + Otsu Thresholding Histogram']
    images2 = [th5, hist1, th6, hist2]
    plt.figure()

    for i in range(4):
        
        if i == 1:
            plt.subplot(2,2,i+1),plt.plot(images2[i])
            plt.axvline(x=otsu1, color='r', linestyle='-')
            plt.xlim([0,256])
        else:
            if i == 3:
                plt.subplot(2,2,i+1),plt.plot(images2[i])
                plt.axvline(x=otsu2, color='r', linestyle='-')
                plt.xlim([0,256])
            else:
                plt.subplot(2,2,i+1),plt.imshow(images2[i],'gray')
                plt.xticks([]),plt.yticks([])
        plt.title(titles[i])
    plt.waitforbuttonpress()
    plt.close('all')

    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

    titles = ['Original Image', 'Otsu thresholding',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th5, th2, th3]

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
