import cv2 as cv
from matplotlib import pyplot as plt


def edges():

    img = cv.imread("./img/moon.jpg", 0)
    edges = cv.Canny(img, 150, 200)

    title = ["Original Image", "Canny"]
    images = [img, edges]

    for i in range(len(images)):
        plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
        plt.title(title[i])
        plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == '__main__':
    edges()
