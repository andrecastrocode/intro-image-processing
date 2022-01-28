#color convertions

import cv2
from matplotlib import pyplot as plt


def load_and_show_image(window_name, path):
    img = cv2.imread(path)
    cv2.imshow(window_name, img)
    return img

def plot_and_show_histogram_color(img):
    color = ('b','g','r')
    plt.figure()
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])


def plot_and_show_histogram_gray(img):
    histr = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.figure()
    plt.plot(histr)
    plt.xlim([0,256])
    
    

def convert_grayscale(img):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img_gray

def convert_and_show_rgb(img):
    img = cv2.resize(img, (0,0), fx=0.5,fy=0.5)
    R = img.copy() 
    G = img.copy()
    B = img.copy()

    G[:,:,0] = G[:,:,2] = 0
    R[:,:,0] = R[:,:,1] = 0
    B[:,:,1] = B[:,:,2] = 0
    R = cv2.cvtColor(R,cv2.COLOR_BGR2GRAY)
    G = cv2.cvtColor(G,cv2.COLOR_BGR2GRAY)
    B = cv2.cvtColor(B,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("i'm blue da ba dee da ba di da ba dee da ba di", B)

def convert_and_show_yuv(img):
    img = cv2.resize(img, (0,0), fx=0.5,fy=0.5)
    Y = img.copy() 
    U = img.copy()
    V = img.copy()

    Y[:,:,1] = Y[:,:,2] = 0
    U[:,:,0] = U[:,:,2] = 0
    V[:,:,0] = V[:,:,1] = 0
    Y = cv2.cvtColor(Y,cv2.COLOR_YUV2BGR)
    U = cv2.cvtColor(U,cv2.COLOR_YUV2BGR)
    V = cv2.cvtColor(V,cv2.COLOR_YUV2BGR)
    Y = cv2.cvtColor(Y,cv2.COLOR_BGR2GRAY)
    U = cv2.cvtColor(U,cv2.COLOR_BGR2GRAY)
    V = cv2.cvtColor(V,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Y", Y)
    cv2.imshow("U", U)
    cv2.imshow("V", V)

def convert_yuv(img):
    img_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
    return img_yuv



def main():

    #original_RGB
    img = load_and_show_image("original","resources/bmw_ix.jpg")
    cv2.waitKey()
    plot_and_show_histogram_color(img)
    plt.waitforbuttonpress()

    #gray
    img_gray = convert_grayscale(img)
    cv2.imshow("grayscale", img_gray)
    cv2.waitKey()

    plot_and_show_histogram_gray(img_gray)
    plt.waitforbuttonpress()

    convert_and_show_rgb(img)
    cv2.waitKey()

    cv2.destroyAllWindows()
    plt.close('all')

    #YUV
    img_yuv = convert_yuv(img)
    cv2.imshow("yuv", img_yuv)
    cv2.waitKey()
    
    convert_and_show_yuv(img_yuv)
    cv2.waitKey()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

