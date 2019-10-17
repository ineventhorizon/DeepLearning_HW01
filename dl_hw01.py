import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#Horizontal flip
def flipHorizontally(img):
    img_horizontally = np.copy(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_horizontally[i][j] = img[i][img.shape[1] - 1 - j]

    return img_horizontally
#Turns the picture to the left
def turn270(img):
    img270 = np.ones((img.shape[1],img.shape[0],img.shape[2]),dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img270[j][i] = img[i][j]
    return img270

#Turns the picture to the right
def turn90(img):
    img90 = np.zeros((img.shape[1], img.shape[0], img.shape[2]),dtype=np.uint8)
    for i in range(0,img.shape[0]): #x 600
        for j in range(0,img.shape[1]): #y 400
            img90[j][img.shape[0]-1-i] = img[i][j]
    return img90
#Reshapes the picture
def reShape(img):
    a = img.shape[0]//2
    b = img.shape[1]//2
    img_reshaped = np.zeros((img.shape[0]//2, img.shape[1]//2, img.shape[2]),dtype=np.uint8)

    for i in range(img.shape[0]//2):
        for j in range(img.shape[1]//2):
            img_reshaped[i][j] = img[i*2][j*2]

    return img_reshaped


img_src = mpimg.imread('cat1.jpg')
#Original Image
img = np.asarray(img_src)
img90 = turn90(img)
img270 = turn270(img)
img_horizontal = flipHorizontally(img)
#Vertical Flip
img_vertical = img[::-1]
img_reshaped = reShape(img)


images = [img, img90,img270,img_horizontal,img_vertical,img_reshaped]

Nc = 2
Nr = 3
fig, axs = plt.subplots(ncols=Nc, nrows=Nr)
fig.suptitle('Deep Learning HW01 / Yusuf Ekrem Kecilioglu')
totalImage = len(images)
imgCount = 0
for i in range(Nr):
    for j in range(Nc):
        if imgCount < totalImage:
            axs[i, j].imshow(images[imgCount])
            if imgCount <=totalImage-3:
                axs[i, j].axis('off')
            imgCount += 1
plt.savefig('result')
plt.show()

